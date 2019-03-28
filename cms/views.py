# -*- coding: utf-8 -*-
from django.shortcuts import (
    render_to_response,
    get_object_or_404,
)
from rest_framework.views import APIView
from .models import Story
from .serializers import StorySerializer
from .utils import paginate, get_obj4fso_cms, get_slug4fso_cms

# Create your views here.

# TODO: YH slug->name 对应关系暂时手动添加
CMS_MAP = {
    "guan-yu-wo-men": "关于我们",
    "gong-si-jian-jie": "公司简介",
    "qi-ye-wen-hua": "企业文化",
    "gong-si-li-nian": "公司理念",
    "he-zuo-huo-ban": "合作伙伴",
    "chan-pin-zhong-xin": "产品中心",
    "ding-zhi-hua-chan-pin": "定制化产品",
    "biao-zhun-hua-chan-pin": "标准化产品",
    "zhu-ying-tui-jian-chan-pin": "主营推荐产品",
    "xin-wen-zhong-xin": "新闻中心",
    "qi-ye-xin-wen": "企业新闻",
    "qi-ye-rong-yu":"企业荣誉",
    "hang-ye-dong-tai": "行业动态",
    "ke-ku-fu-wu": "客户服务",
    "ke-hu-an-li": "客户案例",
    "ren-cai-zhao-pin": "人才招聘",
    "shi-chang-bu": "市场部",
    "yan-fa-bu": "研发部",
    "jing-ying-bu": "经营部",
    "lian-xi-wo-men": "联系我们",
    "lian-xi-liu-bo": "联系六博",
    "ke-hu-liu-yan": "客户留言",

}


def index_view(request):
    """
    网站首页
    :param request:
    :return:
    """
    # 首页展示
    about = get_obj4fso_cms(index_view, "关于我们")
    products = get_obj4fso_cms(index_view, "产品中心")
    news = get_obj4fso_cms(index_view, "新闻中心")
    # 只取slug
    jianie = get_slug4fso_cms("公司简介")
    wenhua = get_slug4fso_cms("企业文化")
    linian = get_slug4fso_cms("公司理念")
    hezuohuoban = get_slug4fso_cms("合作伙伴")
    dingzhihua = get_slug4fso_cms("定制化产品")
    biaozhunhua = get_slug4fso_cms("标准化产品")
    zhuying = get_slug4fso_cms("主营推荐产品")
    qiyexinwen = get_obj4fso_cms(index_view,"企业新闻")
    qiyerongyu = get_obj4fso_cms(index_view,"企业荣誉")
    hangyedongtai = get_slug4fso_cms("行业动态")
    kehufuwu = get_slug4fso_cms("客户服务")
    kehuanli = get_slug4fso_cms("客户案例")
    rencaizhaopin = get_slug4fso_cms("人才招聘")
    shichangbu = get_slug4fso_cms("市场部")
    yanfabu = get_slug4fso_cms("研发部")
    jingyingbu = get_slug4fso_cms("经营部")
    lianxiwomen = get_slug4fso_cms("联系我们")
    lianxiliubo = get_slug4fso_cms("联系六博")
    liuyan = get_slug4fso_cms("客户留言")

    context = {
        "about": about,
        "news": news,
        "products": products,
        # 取自utils
        "jianie": jianie,
        "wenhua": wenhua,
        "linian": linian,
        "huoban": hezuohuoban,
        "dingzhihua": dingzhihua,
        "biaozhunhua": biaozhunhua,
        "zhuying": zhuying,
        "qiyexinwen": qiyexinwen,
        "qiyerongyu":qiyerongyu,
        "hangyedongtai": hangyedongtai,
        "kehufuwu": kehufuwu,
        "kehuanli": kehuanli,
        "rencaizhaopin": rencaizhaopin,
        "shichangbu": shichangbu,
        "yanfabu": yanfabu,
        "jingyingbu": jingyingbu,
        "lianxiwomen": lianxiwomen,
        "lianxiliubo": lianxiliubo,
        "liuyan": liuyan,
    }
    return render_to_response('oce_index.html', context)


class CmsList(APIView):
    """
    通用列表页（未区分二级菜单）
    """

    def get(self, request):
        current_page = request.query_params.get('current_page')
        slug = request.query_params.get('slug')
        print '===slug==', slug
        if not slug:
            # 暂时这样处理， 后期优化
            return render_to_response('404.html')
        name = CMS_MAP.get(slug, '')
        cms_obj = get_obj4fso_cms('cms', name)
        cms = StorySerializer(cms_obj, many=True).data
        # 处理分页
        data = paginate(cms, current_page)
        context = {
            "request": request,
            "data": data,
            "slug": slug
        }
        if slug == "ke-hu-liu-yan":
            return render_to_response('oce_book.html')
        elif slug == "lian-xi-liu-bo" or slug == "lian-xi-wo-men":
            return render_to_response('oce_contact.html')
        elif slug == "zhu-ying-tui-jian-chan-pin" or slug == "ding-zhi-hua-chan-pin" or slug == "biao-zhun-hua-chan-pin" or slug == "zhu-ying-tui-jian":
            print '-=-=-=', data
            return render_to_response('oce_product.html', context)
        return render_to_response('oce_news.html', context)


class CmsDetail(APIView):
    """
    通用详情页
    """

    def get(self, request):
        slug = request.query_params.get('slug')
        print '===', slug
        cms = get_object_or_404(
            Story,
            slug=slug,
            status=3
        )
        if cms:
            cms.hits += 1
            cms.save()
            context = {
                "new": cms,
                "slug": slug
            }
            print context["slug"]
            if cms.category.slug == 'zhu-ying-tui-jian-chan-pin':
                print '===7777777777',
                return render_to_response('oce_product_details.html', context)
            return render_to_response('oce_news_detail.html', context)

        return render_to_response('404.html')


class SearchView(APIView):
    """
    整栈搜索
    """
    def get(self, request):
        if 'q' in request.GET:
            term = request.query_params.get('q')
            story_list = get_obj4fso_cms('search', term)
            heading = "Search results"
        return render_to_response("cms/story_list.html", locals())
