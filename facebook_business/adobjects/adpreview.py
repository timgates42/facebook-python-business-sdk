# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.helpers.adpreviewmixin import AdPreviewMixin

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdPreview(
    AdPreviewMixin,
    AbstractObject,
):

    def __init__(self, api=None):
        super(AdPreview, self).__init__()
        self._isAdPreview = True
        self._api = api

    class Field(AbstractObject.Field):
        body = 'body'
        transformation_spec = 'transformation_spec'

    class AdFormat:
        audience_network_instream_video = 'AUDIENCE_NETWORK_INSTREAM_VIDEO'
        audience_network_instream_video_mobile = 'AUDIENCE_NETWORK_INSTREAM_VIDEO_MOBILE'
        audience_network_outstream_video = 'AUDIENCE_NETWORK_OUTSTREAM_VIDEO'
        audience_network_rewarded_video = 'AUDIENCE_NETWORK_REWARDED_VIDEO'
        biz_disco_feed_mobile = 'BIZ_DISCO_FEED_MOBILE'
        desktop_feed_standard = 'DESKTOP_FEED_STANDARD'
        facebook_reels_banner = 'FACEBOOK_REELS_BANNER'
        facebook_reels_banner_desktop = 'FACEBOOK_REELS_BANNER_DESKTOP'
        facebook_reels_mobile = 'FACEBOOK_REELS_MOBILE'
        facebook_reels_postloop = 'FACEBOOK_REELS_POSTLOOP'
        facebook_reels_sticker = 'FACEBOOK_REELS_STICKER'
        facebook_story_mobile = 'FACEBOOK_STORY_MOBILE'
        facebook_story_sticker_mobile = 'FACEBOOK_STORY_STICKER_MOBILE'
        instagram_explore_contextual = 'INSTAGRAM_EXPLORE_CONTEXTUAL'
        instagram_explore_grid_home = 'INSTAGRAM_EXPLORE_GRID_HOME'
        instagram_explore_immersive = 'INSTAGRAM_EXPLORE_IMMERSIVE'
        instagram_feed_web = 'INSTAGRAM_FEED_WEB'
        instagram_feed_web_m_site = 'INSTAGRAM_FEED_WEB_M_SITE'
        instagram_profile_feed = 'INSTAGRAM_PROFILE_FEED'
        instagram_reels = 'INSTAGRAM_REELS'
        instagram_reels_overlay = 'INSTAGRAM_REELS_OVERLAY'
        instagram_search_chain = 'INSTAGRAM_SEARCH_CHAIN'
        instagram_search_grid = 'INSTAGRAM_SEARCH_GRID'
        instagram_standard = 'INSTAGRAM_STANDARD'
        instagram_story = 'INSTAGRAM_STORY'
        instagram_story_camera_tray = 'INSTAGRAM_STORY_CAMERA_TRAY'
        instagram_story_web = 'INSTAGRAM_STORY_WEB'
        instagram_story_web_m_site = 'INSTAGRAM_STORY_WEB_M_SITE'
        instant_article_recirculation_ad = 'INSTANT_ARTICLE_RECIRCULATION_AD'
        instant_article_standard = 'INSTANT_ARTICLE_STANDARD'
        instream_banner_desktop = 'INSTREAM_BANNER_DESKTOP'
        instream_banner_mobile = 'INSTREAM_BANNER_MOBILE'
        instream_video_desktop = 'INSTREAM_VIDEO_DESKTOP'
        instream_video_image = 'INSTREAM_VIDEO_IMAGE'
        instream_video_mobile = 'INSTREAM_VIDEO_MOBILE'
        job_browser_desktop = 'JOB_BROWSER_DESKTOP'
        job_browser_mobile = 'JOB_BROWSER_MOBILE'
        marketplace_mobile = 'MARKETPLACE_MOBILE'
        messenger_mobile_inbox_media = 'MESSENGER_MOBILE_INBOX_MEDIA'
        messenger_mobile_story_media = 'MESSENGER_MOBILE_STORY_MEDIA'
        mobile_banner = 'MOBILE_BANNER'
        mobile_feed_basic = 'MOBILE_FEED_BASIC'
        mobile_feed_standard = 'MOBILE_FEED_STANDARD'
        mobile_fullwidth = 'MOBILE_FULLWIDTH'
        mobile_interstitial = 'MOBILE_INTERSTITIAL'
        mobile_medium_rectangle = 'MOBILE_MEDIUM_RECTANGLE'
        mobile_native = 'MOBILE_NATIVE'
        right_column_standard = 'RIGHT_COLUMN_STANDARD'
        suggested_video_desktop = 'SUGGESTED_VIDEO_DESKTOP'
        suggested_video_mobile = 'SUGGESTED_VIDEO_MOBILE'
        watch_feed_home = 'WATCH_FEED_HOME'
        watch_feed_mobile = 'WATCH_FEED_MOBILE'

    class CreativeFeature:
        profile_card = 'profile_card'

    class RenderType:
        fallback = 'FALLBACK'

    # @deprecated get_endpoint function is deprecated
    @classmethod
    def get_endpoint(cls):
        return 'previews'

    _field_types = {
        'body': 'string',
        'transformation_spec': 'Object',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        field_enum_info['AdFormat'] = AdPreview.AdFormat.__dict__.values()
        field_enum_info['CreativeFeature'] = AdPreview.CreativeFeature.__dict__.values()
        field_enum_info['RenderType'] = AdPreview.RenderType.__dict__.values()
        return field_enum_info


