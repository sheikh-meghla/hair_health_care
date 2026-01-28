from django.urls import path

from apps.landing_page.views import HowItWorksAdminAPIView, TakeTheGuessworkOutOfHairCareAPIView, TrustAndTransparencyAdminAPIView, FooterSectionAdminAPIView, FeaturesAdminAPIView, HeroSectionAdminAPIView, WhyHairiSafeExistsAdminAPIView

urlpatterns = [
    path('hero-section/', HeroSectionAdminAPIView.as_view(), name='hero-section-admin'),
    path('how-it-works/', HowItWorksAdminAPIView.as_view(), name='how-it-works-admin'),
    path('why-hairisafe-exists/', WhyHairiSafeExistsAdminAPIView.as_view(), name='why-hairisafe-exists-admin'),
    path('features/', FeaturesAdminAPIView.as_view(), name='features-admin'),
    path('trust-and-transparency/', TrustAndTransparencyAdminAPIView.as_view(), name='trust-and-transparency-admin'),
    path('take-the-guesswork-out-of-hair-care/', TakeTheGuessworkOutOfHairCareAPIView.as_view(), name='take-the-guesswork-out-of-hair-care-admin'),
    path('footer-section/', FooterSectionAdminAPIView.as_view(), name='footer-section-admin'),
]