# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdAccountTargetingUnified(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdAccountTargetingUnified = True
        super(AdAccountTargetingUnified, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        audience_size_lower_bound = 'audience_size_lower_bound'
        audience_size_upper_bound = 'audience_size_upper_bound'
        conversion_lift = 'conversion_lift'
        description = 'description'
        id = 'id'
        img = 'img'
        info = 'info'
        info_title = 'info_title'
        is_recommendation = 'is_recommendation'
        key = 'key'
        link = 'link'
        name = 'name'
        parent = 'parent'
        partner = 'partner'
        path = 'path'
        performance_rating = 'performance_rating'
        raw_name = 'raw_name'
        recommendation_model = 'recommendation_model'
        search_interest_id = 'search_interest_id'
        source = 'source'
        spend = 'spend'
        type = 'type'
        valid = 'valid'

    class LimitType:
        behaviors = 'behaviors'
        college_years = 'college_years'
        education_majors = 'education_majors'
        education_schools = 'education_schools'
        education_statuses = 'education_statuses'
        ethnic_affinity = 'ethnic_affinity'
        family_statuses = 'family_statuses'
        generation = 'generation'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        income = 'income'
        industries = 'industries'
        interested_in = 'interested_in'
        interests = 'interests'
        life_events = 'life_events'
        location_categories = 'location_categories'
        moms = 'moms'
        net_worth = 'net_worth'
        office_type = 'office_type'
        politics = 'politics'
        relationship_statuses = 'relationship_statuses'
        user_adclusters = 'user_adclusters'
        work_employers = 'work_employers'
        work_positions = 'work_positions'

    class RegulatedCategories:
        credit = 'CREDIT'
        employment = 'EMPLOYMENT'
        housing = 'HOUSING'
        issues_elections_politics = 'ISSUES_ELECTIONS_POLITICS'
        none = 'NONE'
        online_gambling_and_gaming = 'ONLINE_GAMBLING_AND_GAMING'

    class RegulatedCountries:
        ad = 'AD'
        ae = 'AE'
        af = 'AF'
        ag = 'AG'
        ai = 'AI'
        al = 'AL'
        am = 'AM'
        an = 'AN'
        ao = 'AO'
        aq = 'AQ'
        ar = 'AR'
        value_as = 'AS'
        at = 'AT'
        au = 'AU'
        aw = 'AW'
        ax = 'AX'
        az = 'AZ'
        ba = 'BA'
        bb = 'BB'
        bd = 'BD'
        be = 'BE'
        bf = 'BF'
        bg = 'BG'
        bh = 'BH'
        bi = 'BI'
        bj = 'BJ'
        bl = 'BL'
        bm = 'BM'
        bn = 'BN'
        bo = 'BO'
        bq = 'BQ'
        br = 'BR'
        bs = 'BS'
        bt = 'BT'
        bv = 'BV'
        bw = 'BW'
        by = 'BY'
        bz = 'BZ'
        ca = 'CA'
        cc = 'CC'
        cd = 'CD'
        cf = 'CF'
        cg = 'CG'
        ch = 'CH'
        ci = 'CI'
        ck = 'CK'
        cl = 'CL'
        cm = 'CM'
        cn = 'CN'
        co = 'CO'
        cr = 'CR'
        cu = 'CU'
        cv = 'CV'
        cw = 'CW'
        cx = 'CX'
        cy = 'CY'
        cz = 'CZ'
        de = 'DE'
        dj = 'DJ'
        dk = 'DK'
        dm = 'DM'
        do = 'DO'
        dz = 'DZ'
        ec = 'EC'
        ee = 'EE'
        eg = 'EG'
        eh = 'EH'
        er = 'ER'
        es = 'ES'
        et = 'ET'
        fi = 'FI'
        fj = 'FJ'
        fk = 'FK'
        fm = 'FM'
        fo = 'FO'
        fr = 'FR'
        ga = 'GA'
        gb = 'GB'
        gd = 'GD'
        ge = 'GE'
        gf = 'GF'
        gg = 'GG'
        gh = 'GH'
        gi = 'GI'
        gl = 'GL'
        gm = 'GM'
        gn = 'GN'
        gp = 'GP'
        gq = 'GQ'
        gr = 'GR'
        gs = 'GS'
        gt = 'GT'
        gu = 'GU'
        gw = 'GW'
        gy = 'GY'
        hk = 'HK'
        hm = 'HM'
        hn = 'HN'
        hr = 'HR'
        ht = 'HT'
        hu = 'HU'
        id = 'ID'
        ie = 'IE'
        il = 'IL'
        im = 'IM'
        value_in = 'IN'
        io = 'IO'
        iq = 'IQ'
        ir = 'IR'
        value_is = 'IS'
        it = 'IT'
        je = 'JE'
        jm = 'JM'
        jo = 'JO'
        jp = 'JP'
        ke = 'KE'
        kg = 'KG'
        kh = 'KH'
        ki = 'KI'
        km = 'KM'
        kn = 'KN'
        kp = 'KP'
        kr = 'KR'
        kw = 'KW'
        ky = 'KY'
        kz = 'KZ'
        la = 'LA'
        lb = 'LB'
        lc = 'LC'
        li = 'LI'
        lk = 'LK'
        lr = 'LR'
        ls = 'LS'
        lt = 'LT'
        lu = 'LU'
        lv = 'LV'
        ly = 'LY'
        ma = 'MA'
        mc = 'MC'
        md = 'MD'
        me = 'ME'
        mf = 'MF'
        mg = 'MG'
        mh = 'MH'
        mk = 'MK'
        ml = 'ML'
        mm = 'MM'
        mn = 'MN'
        mo = 'MO'
        mp = 'MP'
        mq = 'MQ'
        mr = 'MR'
        ms = 'MS'
        mt = 'MT'
        mu = 'MU'
        mv = 'MV'
        mw = 'MW'
        mx = 'MX'
        my = 'MY'
        mz = 'MZ'
        na = 'NA'
        nc = 'NC'
        ne = 'NE'
        nf = 'NF'
        ng = 'NG'
        ni = 'NI'
        nl = 'NL'
        no = 'NO'
        np = 'NP'
        nr = 'NR'
        nu = 'NU'
        nz = 'NZ'
        om = 'OM'
        pa = 'PA'
        pe = 'PE'
        pf = 'PF'
        pg = 'PG'
        ph = 'PH'
        pk = 'PK'
        pl = 'PL'
        pm = 'PM'
        pn = 'PN'
        pr = 'PR'
        ps = 'PS'
        pt = 'PT'
        pw = 'PW'
        py = 'PY'
        qa = 'QA'
        re = 'RE'
        ro = 'RO'
        rs = 'RS'
        ru = 'RU'
        rw = 'RW'
        sa = 'SA'
        sb = 'SB'
        sc = 'SC'
        sd = 'SD'
        se = 'SE'
        sg = 'SG'
        sh = 'SH'
        si = 'SI'
        sj = 'SJ'
        sk = 'SK'
        sl = 'SL'
        sm = 'SM'
        sn = 'SN'
        so = 'SO'
        sr = 'SR'
        ss = 'SS'
        st = 'ST'
        sv = 'SV'
        sx = 'SX'
        sy = 'SY'
        sz = 'SZ'
        tc = 'TC'
        td = 'TD'
        tf = 'TF'
        tg = 'TG'
        th = 'TH'
        tj = 'TJ'
        tk = 'TK'
        tl = 'TL'
        tm = 'TM'
        tn = 'TN'
        to = 'TO'
        tr = 'TR'
        tt = 'TT'
        tv = 'TV'
        tw = 'TW'
        tz = 'TZ'
        ua = 'UA'
        ug = 'UG'
        um = 'UM'
        us = 'US'
        uy = 'UY'
        uz = 'UZ'
        va = 'VA'
        vc = 'VC'
        ve = 'VE'
        vg = 'VG'
        vi = 'VI'
        vn = 'VN'
        vu = 'VU'
        wf = 'WF'
        ws = 'WS'
        xk = 'XK'
        ye = 'YE'
        yt = 'YT'
        za = 'ZA'
        zm = 'ZM'
        zw = 'ZW'

    class WhitelistedTypes:
        adgroup_id = 'adgroup_id'
        age_max = 'age_max'
        age_min = 'age_min'
        age_range = 'age_range'
        alternate_auto_targeting_option = 'alternate_auto_targeting_option'
        app_install_state = 'app_install_state'
        audience_network_positions = 'audience_network_positions'
        behaviors = 'behaviors'
        brand_safety_content_filter_levels = 'brand_safety_content_filter_levels'
        brand_safety_content_severity_levels = 'brand_safety_content_severity_levels'
        cafe_ca_contraction_targeting_signal = 'cafe_ca_contraction_targeting_signal'
        cafe_ca_expansion_targeting_signal = 'cafe_ca_expansion_targeting_signal'
        catalog_based_targeting = 'catalog_based_targeting'
        cities = 'cities'
        city_keys = 'city_keys'
        college_years = 'college_years'
        conjunctive_user_adclusters = 'conjunctive_user_adclusters'
        connections = 'connections'
        contextual_targeting_categories = 'contextual_targeting_categories'
        countries = 'countries'
        country = 'country'
        country_groups = 'country_groups'
        custom_audiences = 'custom_audiences'
        device_platforms = 'device_platforms'
        direct_install_devices = 'direct_install_devices'
        dynamic_audience_ids = 'dynamic_audience_ids'
        education_majors = 'education_majors'
        education_schools = 'education_schools'
        education_statuses = 'education_statuses'
        effective_audience_network_positions = 'effective_audience_network_positions'
        effective_device_platforms = 'effective_device_platforms'
        effective_facebook_positions = 'effective_facebook_positions'
        effective_instagram_positions = 'effective_instagram_positions'
        effective_messenger_positions = 'effective_messenger_positions'
        effective_oculus_positions = 'effective_oculus_positions'
        effective_publisher_platforms = 'effective_publisher_platforms'
        effective_whatsapp_positions = 'effective_whatsapp_positions'
        engagement_specs = 'engagement_specs'
        ethnic_affinity = 'ethnic_affinity'
        exclude_previous_days = 'exclude_previous_days'
        exclude_reached_since = 'exclude_reached_since'
        excluded_brand_safety_content_types = 'excluded_brand_safety_content_types'
        excluded_connections = 'excluded_connections'
        excluded_custom_audiences = 'excluded_custom_audiences'
        excluded_dynamic_audience_ids = 'excluded_dynamic_audience_ids'
        excluded_engagement_specs = 'excluded_engagement_specs'
        excluded_geo_locations = 'excluded_geo_locations'
        excluded_mobile_device_model = 'excluded_mobile_device_model'
        excluded_product_audience_specs = 'excluded_product_audience_specs'
        excluded_publisher_categories = 'excluded_publisher_categories'
        excluded_publisher_list_ids = 'excluded_publisher_list_ids'
        excluded_user_adclusters = 'excluded_user_adclusters'
        excluded_user_device = 'excluded_user_device'
        exclusions = 'exclusions'
        facebook_positions = 'facebook_positions'
        family_statuses = 'family_statuses'
        fb_deal_id = 'fb_deal_id'
        flexible_spec = 'flexible_spec'
        follow_profiles = 'follow_profiles'
        follow_profiles_negative = 'follow_profiles_negative'
        format = 'format'
        friends_of_connections = 'friends_of_connections'
        gatekeepers = 'gatekeepers'
        genders = 'genders'
        generation = 'generation'
        geo_locations = 'geo_locations'
        home_ownership = 'home_ownership'
        home_type = 'home_type'
        home_value = 'home_value'
        household_composition = 'household_composition'
        id = 'id'
        income = 'income'
        industries = 'industries'
        instagram_hashtags = 'instagram_hashtags'
        instagram_positions = 'instagram_positions'
        instream_video_skippable_excluded = 'instream_video_skippable_excluded'
        instream_video_sponsorship_placements = 'instream_video_sponsorship_placements'
        interest_defaults_source = 'interest_defaults_source'
        interested_in = 'interested_in'
        interests = 'interests'
        is_instagram_destination_ad = 'is_instagram_destination_ad'
        is_whatsapp_destination_ad = 'is_whatsapp_destination_ad'
        keywords = 'keywords'
        life_events = 'life_events'
        locales = 'locales'
        location_categories = 'location_categories'
        location_cluster_ids = 'location_cluster_ids'
        location_expansion = 'location_expansion'
        marketplace_product_categories = 'marketplace_product_categories'
        messenger_positions = 'messenger_positions'
        mobile_device_model = 'mobile_device_model'
        moms = 'moms'
        net_worth = 'net_worth'
        oculus_positions = 'oculus_positions'
        office_type = 'office_type'
        page_types = 'page_types'
        place_page_set_ids = 'place_page_set_ids'
        political_views = 'political_views'
        politics = 'politics'
        product_audience_specs = 'product_audience_specs'
        prospecting_audience = 'prospecting_audience'
        publisher_platforms = 'publisher_platforms'
        radius = 'radius'
        region_keys = 'region_keys'
        regions = 'regions'
        relationship_statuses = 'relationship_statuses'
        rtb_flag = 'rtb_flag'
        site_category = 'site_category'
        targeting_automation = 'targeting_automation'
        targeting_optimization = 'targeting_optimization'
        targeting_relaxation_types = 'targeting_relaxation_types'
        timezones = 'timezones'
        topic = 'topic'
        trending = 'trending'
        user_adclusters = 'user_adclusters'
        user_device = 'user_device'
        user_event = 'user_event'
        user_os = 'user_os'
        user_page_threads = 'user_page_threads'
        user_page_threads_excluded = 'user_page_threads_excluded'
        whatsapp_positions = 'whatsapp_positions'
        wireless_carrier = 'wireless_carrier'
        work_employers = 'work_employers'
        work_positions = 'work_positions'
        zips = 'zips'

    class AppStore:
        amazon_app_store = 'amazon_app_store'
        apk_mirror = 'apk_mirror'
        apk_monk = 'apk_monk'
        apk_pure = 'apk_pure'
        aptoide_a1_store = 'aptoide_a1_store'
        bemobi_mobile_store = 'bemobi_mobile_store'
        does_not_exist = 'does_not_exist'
        fb_android_store = 'fb_android_store'
        fb_canvas = 'fb_canvas'
        fb_gameroom = 'fb_gameroom'
        galaxy_store = 'galaxy_store'
        google_play = 'google_play'
        instant_game = 'instant_game'
        itunes = 'itunes'
        itunes_ipad = 'itunes_ipad'
        neon_android_store = 'neon_android_store'
        none = 'none'
        oculus_app_store = 'oculus_app_store'
        oppo = 'oppo'
        roku_channel_store = 'roku_channel_store'
        uptodown = 'uptodown'
        vivo = 'vivo'
        windows_10_store = 'windows_10_store'
        windows_store = 'windows_store'
        xiaomi = 'xiaomi'

    class Objective:
        app_installs = 'APP_INSTALLS'
        brand_awareness = 'BRAND_AWARENESS'
        conversions = 'CONVERSIONS'
        event_responses = 'EVENT_RESPONSES'
        lead_generation = 'LEAD_GENERATION'
        link_clicks = 'LINK_CLICKS'
        local_awareness = 'LOCAL_AWARENESS'
        messages = 'MESSAGES'
        offer_claims = 'OFFER_CLAIMS'
        outcome_app_promotion = 'OUTCOME_APP_PROMOTION'
        outcome_awareness = 'OUTCOME_AWARENESS'
        outcome_engagement = 'OUTCOME_ENGAGEMENT'
        outcome_leads = 'OUTCOME_LEADS'
        outcome_sales = 'OUTCOME_SALES'
        outcome_traffic = 'OUTCOME_TRAFFIC'
        page_likes = 'PAGE_LIKES'
        post_engagement = 'POST_ENGAGEMENT'
        product_catalog_sales = 'PRODUCT_CATALOG_SALES'
        reach = 'REACH'
        store_visits = 'STORE_VISITS'
        video_views = 'VIDEO_VIEWS'

    class Mode:
        best_performing = 'best_performing'
        recently_used = 'recently_used'
        related = 'related'
        suggestions = 'suggestions'

    _field_types = {
        'audience_size_lower_bound': 'unsigned int',
        'audience_size_upper_bound': 'unsigned int',
        'conversion_lift': 'float',
        'description': 'string',
        'id': 'string',
        'img': 'string',
        'info': 'string',
        'info_title': 'string',
        'is_recommendation': 'bool',
        'key': 'string',
        'link': 'string',
        'name': 'string',
        'parent': 'string',
        'partner': 'string',
        'path': 'list<string>',
        'performance_rating': 'unsigned int',
        'raw_name': 'string',
        'recommendation_model': 'string',
        'search_interest_id': 'string',
        'source': 'string',
        'spend': 'float',
        'type': 'string',
        'valid': 'bool',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['LimitType'] = AdAccountTargetingUnified.LimitType.__dict__.values()
        field_enum_info['RegulatedCategories'] = AdAccountTargetingUnified.RegulatedCategories.__dict__.values()
        field_enum_info['RegulatedCountries'] = AdAccountTargetingUnified.RegulatedCountries.__dict__.values()
        field_enum_info['WhitelistedTypes'] = AdAccountTargetingUnified.WhitelistedTypes.__dict__.values()
        field_enum_info['AppStore'] = AdAccountTargetingUnified.AppStore.__dict__.values()
        field_enum_info['Objective'] = AdAccountTargetingUnified.Objective.__dict__.values()
        field_enum_info['Mode'] = AdAccountTargetingUnified.Mode.__dict__.values()
        return field_enum_info


