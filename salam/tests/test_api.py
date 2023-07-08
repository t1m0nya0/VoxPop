import requests


def test_get_comments():
    expected = {
        "paginated_comments": [
            {
                "text": "saaaaalam",
                "category": {
                    "positive": True,
                    "negative": False
                }
            }
        ]
    }
    response = requests.get("http://localhost:8000/comments")

    assert response.status_code == 200
    assert response.json() == expected


# def test_create_comment():
#     comment_data = {
#         "text": "saaaaalam",
#         "category": {
#             "positive": True,
#             "negative": False
#         }
#     }
#     response = requests.post(
#         "http://localhost:8000/comments", data=comment_data
#     )
#     assert response.status_code == 200
#
#     response_json = response.json()
#     assert "message" in response_json
#     assert response_json["message"] == "Item created"
