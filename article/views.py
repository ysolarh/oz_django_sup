import json
from http.client import BAD_REQUEST

from django.http import HttpRequest, JsonResponse
from django.views import View

from services import create_comment_service


class CommentView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        try:
            body = json.loads(request.body)
        except JsonDecodeError:
            return JsonResponse({'error': ["Json 형식 아님"]}, status=BAD_REQUEST)

        # 공부할것
        # Request DTO
        # pydantic
        # 에러처리 실행하는 단위테스트 만들어야함 -> 숙제


        # elif isinstance(body["article_id"], int):
        # return JsonResponse({"error": ["author가 없습니다."]}, status=400)

        if "author" not in body:
            return JsonResponse({"error": ["author가 없습니다."]}, status=400)

        if "body" not in body:
            return JsonResponse({"error": ["body가 없습니다."]}, status=400)

        comment = create_comment_service(
            body["article_id"],
            body["author"],
            body["body"],
        )
        return JsonResponse({"comment_id": comment.id})
