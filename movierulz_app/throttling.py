from rest_framework.throttling import UserRateThrottle


class ReviewDetailThrottle(UserRateThrottle):
    scope = 'review_detail'
