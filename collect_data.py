import ast
import json
import os

import requests
from bs4 import BeautifulSoup

api_key: str = os.environ.get("STACK_API_KEY")
vyxal_characters = """'Jk\xaf\u01d4\u1e03\u0226"2=%/\u1e44\u2026\xa3D\u1e8bY.\u207dqG\u207c\u1e0a\u1e61\u27c7^\xa8o\u221e\u2080Ty\u1e8a\xdfP\u03c4\u022fFM\xbe\u1e0b\u0192\u20813U\xb99\u2085#\u010a\u0281N\u21b3)Ez\u017b\u2264\xa5\u2105i]\U0001f36a\u27e8\xa6\u230a\u2229\u01cd5\u25a1\ua60d\u2248\xf0\u027d\u1e87W\u1e8f\u01d38\u2087X!\u1e58\u019b\u03b5\u0256\u1e22\u0d9ee\u2021\u2206\u01ce|js\xbc?\u2227\u1e45\xa1<[w:\u1e6a{t`n;\xb6\u2193\u1e6b\u226cu\u01d0&\u20ac\xa4\xbd\u2237\u2088\xac\u01d2\u0140\u03bb\u2022\xa2av\xa74\u2083\u1e86\u2191l$>g\u2082\u2234\u01211\u1e60\u21e9\xb1\xb0C\xde\u0280\u1e1f\u0117\u017c\u022e\xb2\u27e9\u1e02S\u22cf\u03a0}\u208c\\\u21e7\u201f\u0227Q\u2228Z@\xb5\u22600\u2310B\u204b\u1e1e\u2070~7\u2308\u010b\u2086\u0116\u208d\ua71db\u215b\u203aOr\u2194f\u1e57h\u2211\u22ced\u1e41\u027e\u22656\u20b4\u222a\u21b2I\xbbK,\u1e2d\xe6\u201b\xd7\u221a\u2084\xabp\u0130c\u01d1\u2235\'\xf8m\u1e23*\u2020R\u21b5V(L\u013f\u2192\xf7_\u201e\u1e56\u2039+x\u1e59\u1e40\u228d\u27d1\u2190H\u0120\u207aA\u03b2\u0188\u01cf-\u2424\u1e8e\u2207'"""  # noqa: E501
post_filter: str = "!7gW7W8.hCz.w3RaMu5gZJ)KKPzO4pFALfq"
page_size = 30

if True:
    page = 1
    with open("post_ids.txt", "a") as f:
        items = True
        while items:
            response = requests.get(
                "https://api.stackexchange.com/2.3/search/excerpts",
                params={
                    "key": api_key,
                    "q": "vyxal is:answer",
                    "site": "codegolf",
                    "page": str(page),
                },
                headers={"accept": "application/JSON"},
            )

            print(response)

            items = response.json()["items"]

            for item in items:
                print(f"{item['answer_id']} {item['body']!r}", file=f)
            page += 1


with open("post_ids.txt") as f:
    posts: list[str] = []
    ids: list[int] = []

    nr_raw = 0
    nr_filtered = 0
    nr_with_code = 0

    for line in f:
        post_id, *contents = line.lower().split()
        post_id = int(post_id)
        contents = ast.literal_eval(" ".join(contents))

        nr_raw += 1
        if "vyxal" in [i.strip(",") for i in contents.split()[:6]]:
            # print(post_id, end=" ")

            ids.append(post_id)
            nr_filtered += 1
        print()
    print(len(ids), (len(ids) + 99) // 100)
    for i in range((len(ids) + page_size - 1) // page_size):
        res = requests.get(
            "https://api.stackexchange.com/2.3/answers/"
            + ";".join(str(i) for i in ids[i * page_size: i * page_size + page_size]),
            params={"key": api_key, "site": "codegolf", "filter": post_filter},
        )

        data = res.json()

        if len(data["items"]) < page_size:
            print(f'warning: loaded only {len(data["items"])=} items')
            # exit()

        for post in data["items"]:
            parsed_content = BeautifulSoup(post["body"], "html.parser")
            code_elements = [
                *parsed_content.select("pre code"),
                *parsed_content.select("code"),
            ]
            if len(code_elements) >= 1:
                posts.append(code_elements[0].string or "")
                nr_with_code += 1

            else:
                print(parsed_content)
                # exit()

    print(f"raw:      {nr_raw:>6}")
    print(f"filtered: {nr_filtered:>6}")
    print(f"code:     {nr_with_code:>6}")

    with open("code_json.json", "w") as f:
        json.dump(posts, f)
