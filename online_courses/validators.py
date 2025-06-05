from rest_framework.serializers import ValidationError


class VideoValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        word = "youtube.com"
        video_link = dict(value).get(self.field)

        if video_link and word not in video_link:
            raise ValidationError("Неверная ссылка на видео")
