import json
from http.client import BAD_REQUEST
from json import JSONDecodeError

from django.http import HttpRequest, JsonResponse
from django.views import View

from services import create_comment_service


class CommentView(View):
    def post(self, request: HttpRequest) -> JsonResponse:
        errors = []
        try:
            body = json.loads(request.body)
            # print(body)
        except JSONDecodeError:
            # return JsonResponse({"error": ["Json 형식 아님"]}, status=BAD_REQUEST)
            errors.append("JSON 형식이 아닙니다.")

        # 공부할것
        # Request DTO
        # pydantic
        # 에러처리 실행하는 단위테스트 만들어야함 -> 숙제

        # if "article_id" not in body:
        #     return JsonResponse({"error": ["article_id가 없습니다."]}, status=400)
        # elif isinstance(body["article_id"], int):
        #     return JsonResponse({"error": ["article_id가 int가 아님"]}, status=400)
        #
        # if "author" not in body:
        #     return JsonResponse({"error": ["author가 없습니다."]}, status=400)
        #
        # if "body" not in body:
        #     return JsonResponse({"error": ["body가 없습니다."]}, status=400)

        if "article_id" not in body:
            errors.append("article_id 가 없습니다.")
        elif not isinstance(body["article_id"], int):
            errors.append(f"article_id 는 정수 여야 합니다. 전달된 값: {body['article_id']}")
        if "author" not in body:
            errors.append("author 가 없습니다.")
        elif not isinstance(body["author"], str):
            errors.append(f"author 는 문자열이어야 합니다. 전달된 값: {body['author']}")
        if "body" not in body:
            errors.append("body 가 없습니다.")
        elif not isinstance(body["body"], str):
            errors.append(f"body 는 문자열 여야 합니다. 전달된 값: {body['body']}")

        if errors:
            return JsonResponse({"errors": errors}, status=BAD_REQUEST)

        comment = create_comment_service(
            body["article_id"],
            body["author"],
            body["body"],
        )
        return JsonResponse({"comment_id": comment.id})
