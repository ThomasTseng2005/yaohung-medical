import os
import re
import time
from datetime import datetime
from functools import lru_cache

from flask import Flask, Response, abort, render_template, request, send_from_directory
from werkzeug.middleware.proxy_fix import ProxyFix
from article_metadata import ARTICLE_SEO_METADATA

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        return False

load_dotenv()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

SITE_NAME = "曜弘診所"
SITE_LOCALE = "zh_TW"
SITE_LANGUAGE = "zh-Hant"
DEFAULT_OG_IMAGE = "/static/header_2025.jpg"
DEFAULT_DESCRIPTION = (
    "曜弘診所位於新北市三重區，提供胃腸肝膽專科、內視鏡檢查、腹部超音波、"
    "週一至週六門診與線上預約服務，整合社區醫療與高階檢查設備。"
)
CLINIC_INFO = {
    "name": SITE_NAME,
    "telephone": "+886-2-2984-0101",
    "display_phone": "02-2984-0101",
    "street_address": "新北市三重區重新路三段107號1樓",
    "postal_code": "241",
    "address_locality": "三重區",
    "address_region": "新北市",
    "address_country": "TW",
    "latitude": 25.0597389,
    "longitude": 121.4911950,
    "same_as": [
        "https://www.facebook.com/%E6%9B%9C%E5%BC%98%E8%A8%BA%E6%89%80-107804257586464/",
        "https://line.me/R/ti/p/%40760nrqdx",
    ],
    "opening_hours": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "https://schema.org/Monday",
                "https://schema.org/Tuesday",
                "https://schema.org/Wednesday",
                "https://schema.org/Thursday",
                "https://schema.org/Friday",
            ],
            "opens": "09:00",
            "closes": "13:00",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "https://schema.org/Monday",
                "https://schema.org/Tuesday",
                "https://schema.org/Wednesday",
                "https://schema.org/Thursday",
                "https://schema.org/Friday",
            ],
            "opens": "14:00",
            "closes": "17:00",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "https://schema.org/Monday",
                "https://schema.org/Tuesday",
                "https://schema.org/Wednesday",
                "https://schema.org/Thursday",
                "https://schema.org/Friday",
            ],
            "opens": "17:30",
            "closes": "21:00",
        },
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
                "https://schema.org/Saturday",
            ],
            "opens": "09:00",
            "closes": "13:00",
        },
    ],
}
PAGE_METADATA = {
    "home": {
        "title": "三重胃腸肝膽專科與內視鏡檢查",
        "description": DEFAULT_DESCRIPTION,
        "path": "/",
        "image": DEFAULT_OG_IMAGE,
        "type": "website",
    },
    "about": {
        "title": "關於我們",
        "description": (
            "認識曜弘診所的醫療理念、醫師背景與社區照護方向，了解三重在地的"
            "胃腸肝膽與內科服務。"
        ),
        "path": "/about",
        "image": "/static/about-header3.jpg",
        "type": "website",
    },
    "equipment": {
        "title": "專業設備",
        "description": (
            "曜弘診所引進高階內視鏡、CAD EYE AI 輔助判讀與超音波設備，提升檢查"
            "準確度與病灶早期發現率。"
        ),
        "path": "/equipment",
        "image": "/static/equipment-header.jpg",
        "type": "website",
    },
    "appointment": {
        "title": "門診預約",
        "description": "查看曜弘診所門診預約、掛號與報到方式，快速安排看診或檢查。",
        "path": "/appointment",
        "image": DEFAULT_OG_IMAGE,
        "type": "website",
    },
    "online_appointment": {
        "title": "網路預約",
        "description": "透過曜弘診所官方預約系統查看網路掛號須知、預約入口與就診提醒。",
        "path": "/online-appointment",
        "image": DEFAULT_OG_IMAGE,
        "type": "website",
    },
    "events": {
        "title": "看診進度",
        "description": "查看曜弘診所目前看診進度與候診資訊，安排到診時間更有效率。",
        "path": "/events",
        "image": DEFAULT_OG_IMAGE,
        "type": "website",
    },
    "environment": {
        "title": "溫馨環境",
        "description": "瀏覽曜弘診所的候診與檢查環境，了解診所空間與就診動線。",
        "path": "/environment",
        "image": "/static/environment-header.jpg",
        "type": "website",
    },
    "articles": {
        "title": "曜弘報報",
        "description": (
            "曜弘診所整理胃腸肝膽、內視鏡檢查與健康衛教文章，提供病人與家屬"
            "清楚可讀的醫療資訊。"
        ),
        "path": "/articles",
        "image": DEFAULT_OG_IMAGE,
        "type": "website",
    },
    "contact": {
        "title": "聯絡我們",
        "description": (
            "查看曜弘診所地址、電話、門診時間與交通資訊，快速找到新北市三重區"
            "的診所位置。"
        ),
        "path": "/contact",
        "image": "/static/contact-header.jpg",
        "type": "website",
    },
}


def iso_timestamp(file_path):
    return datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d")


def strip_html(text):
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def trim_description(text, limit=160):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    shortened = text[: limit - 1].rsplit(" ", 1)[0].strip()
    return f"{shortened}…"


def get_site_url():
    configured = os.getenv("SITE_URL", "").strip().rstrip("/")
    if configured:
        return configured
    return request.url_root.rstrip("/")


def absolute_url(path):
    if not path:
        return get_site_url()
    if path.startswith("http://") or path.startswith("https://"):
        return path
    if not path.startswith("/"):
        path = f"/{path}"
    return f"{get_site_url()}{path}"


@lru_cache(maxsize=1)
def get_article_metadata():
    article_dir = os.path.join(app.root_path, "templates", "articles")
    articles = {}

    for name in sorted(os.listdir(article_dir)):
        if not name.endswith(".html"):
            continue

        slug = name[:-5]
        file_path = os.path.join(article_dir, name)
        content = open(file_path, encoding="utf-8").read()
        configured_metadata = ARTICLE_SEO_METADATA.get(slug, {})
        headline_match = re.search(
            r'<div class="article-detail-title">\s*<h[12]>(.*?)</h[12]>',
            content,
            re.S,
        )
        paragraphs = [
            strip_html(match)
            for match in re.findall(r"<p[^>]*>(.*?)</p>", content, re.S)
        ]
        paragraphs = [
            paragraph
            for paragraph in paragraphs
            if paragraph and paragraph not in {"曜弘報報", "聯絡我們"}
        ]
        image_match = re.search(
            r"filename='([^']+\.(?:jpg|jpeg|png|webp))'",
            content,
            re.I,
        )

        headline = (
            strip_html(headline_match.group(1))
            if headline_match
            else slug.replace("-", " ")
        )
        title = configured_metadata.get("title", headline)
        description = configured_metadata.get(
            "description",
            trim_description(" ".join(paragraphs[:2])) or DEFAULT_DESCRIPTION,
        )
        keywords = configured_metadata.get("keywords", "")
        image = configured_metadata.get("image")
        if not image:
            image = f"/static/{image_match.group(1)}" if image_match else DEFAULT_OG_IMAGE

        articles[slug] = {
            "title": title,
            "headline": headline,
            "description": description,
            "keywords": keywords,
            "image": image,
            "path": f"/articles/{slug}",
            "type": "article",
            "date_modified": iso_timestamp(file_path),
        }

    return articles


def build_seo(page_key, article_slug=None):
    metadata = PAGE_METADATA[page_key].copy()
    if article_slug:
        metadata.update(get_article_metadata()[article_slug])

    title = metadata["title"]
    metadata["full_title"] = (
        SITE_NAME if title == SITE_NAME else f"{title} | {SITE_NAME}"
    )
    metadata["site_name"] = SITE_NAME
    metadata["locale"] = SITE_LOCALE
    metadata["language"] = SITE_LANGUAGE
    metadata["canonical_url"] = absolute_url(metadata["path"])
    metadata["image_url"] = absolute_url(metadata.get("image", DEFAULT_OG_IMAGE))
    metadata["robots"] = "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    return metadata


def clinic_structured_data():
    return {
        "@context": "https://schema.org",
        "@type": "MedicalClinic",
        "@id": absolute_url("/#medical-clinic"),
        "name": CLINIC_INFO["name"],
        "url": absolute_url("/"),
        "image": absolute_url(DEFAULT_OG_IMAGE),
        "description": DEFAULT_DESCRIPTION,
        "telephone": CLINIC_INFO["telephone"],
        "medicalSpecialty": ["Gastroenterologic", "InternalMedicine"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CLINIC_INFO["street_address"],
            "addressLocality": CLINIC_INFO["address_locality"],
            "addressRegion": CLINIC_INFO["address_region"],
            "postalCode": CLINIC_INFO["postal_code"],
            "addressCountry": CLINIC_INFO["address_country"],
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": CLINIC_INFO["latitude"],
            "longitude": CLINIC_INFO["longitude"],
        },
        "sameAs": CLINIC_INFO["same_as"],
        "openingHoursSpecification": CLINIC_INFO["opening_hours"],
        "availableLanguage": ["zh-TW"],
        "hasMap": absolute_url("/contact"),
    }


def website_structured_data():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": absolute_url("/#website"),
        "url": absolute_url("/"),
        "name": SITE_NAME,
        "inLanguage": SITE_LANGUAGE,
        "publisher": {"@id": absolute_url("/#medical-clinic")},
    }


def article_structured_data(article_slug):
    article = get_article_metadata()[article_slug]
    return {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["headline"],
        "description": article["description"],
        "image": [absolute_url(article["image"])],
        "author": {
            "@type": "Organization",
            "name": SITE_NAME,
        },
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "logo": {
                "@type": "ImageObject",
                "url": absolute_url("/static/ms-icon-310x310.png"),
            },
        },
        "mainEntityOfPage": absolute_url(article["path"]),
        "dateModified": article["date_modified"],
        "inLanguage": SITE_LANGUAGE,
    }


def breadcrumb_structured_data(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": position,
                "name": item["name"],
                "item": absolute_url(item["path"]),
            }
            for position, item in enumerate(items, start=1)
        ],
    }


def render_page(template_name, page_key, **context):
    seo = build_seo(page_key, context.get("article_slug"))
    structured_data = [clinic_structured_data(), website_structured_data()]

    if seo["type"] == "article":
        article_slug = context["article_slug"]
        structured_data.append(article_structured_data(article_slug))
        structured_data.append(
            breadcrumb_structured_data(
                [
                    {"name": "首頁", "path": "/"},
                    {"name": "曜弘報報", "path": "/articles"},
                    {"name": seo["headline"], "path": seo["path"]},
                ]
            )
        )
    elif seo["path"] != "/":
        structured_data.append(
            breadcrumb_structured_data(
                [
                    {"name": "首頁", "path": "/"},
                    {"name": seo["title"], "path": seo["path"]},
                ]
            )
        )
    else:
        structured_data.append(
            breadcrumb_structured_data(
                [
                    {"name": "首頁", "path": "/"},
                ]
            )
        )

    return render_template(
        template_name,
        seo=seo,
        structured_data=structured_data,
        clinic=CLINIC_INFO,
        title=seo["title"],
        **context,
    )


@app.context_processor
def inject_timestamp():
    return {"timestamp": int(time.time())}


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "ms-icon-310x310.png",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/robots.txt")
def robots_txt():
    return Response(
        "\n".join(
            [
                "User-agent: *",
                "Allow: /",
                f"Sitemap: {absolute_url('/sitemap.xml')}",
            ]
        ),
        mimetype="text/plain",
    )


@app.route("/sitemap.xml")
def sitemap_xml():
    routes = []
    for key, metadata in PAGE_METADATA.items():
        if key == "online_appointment":
            routes.append((metadata["path"], iso_timestamp(__file__)))
            continue
        routes.append((metadata["path"], iso_timestamp(__file__)))

    for article in get_article_metadata().values():
        routes.append((article["path"], article["date_modified"]))

    sitemap = render_template("sitemap.xml", routes=routes, absolute_url=absolute_url)
    return Response(sitemap, mimetype="application/xml")


@app.route("/")
def home():
    return render_page("home.html", "home", navbar="trans", footer="0rem", footer_two="0rem")


@app.route("/about")
def about():
    return render_page("about.html", "about", navbar="green", footer="3rem", footer_two="3rem")


@app.route("/equipment")
def equipment():
    return render_page("equipment.html", "equipment", navbar="green", footer="3rem", footer_two="3rem")


@app.route("/appointment")
def appointment():
    return render_page("appointment.html", "appointment", navbar="green", footer="7.5rem", footer_two="7.5rem")


@app.route("/online-appointment")
def online_appointment():
    return render_page("online-appointment.html", "online_appointment", navbar="green", footer="7.5rem", footer_two="7.5rem")


@app.route("/events")
def events():
    return render_page("events.html", "events", navbar="green", footer="7.5rem", footer_two="7.5rem")


@app.route("/environment")
def environment():
    return render_page("environment.html", "environment", navbar="green", footer="0", footer_two="0")


@app.route("/articles")
def articles():
    return render_page("articles.html", "articles", navbar="green", footer="0", footer_two="0")


@app.route("/articles/<article>")
def article(article):
    article_metadata = get_article_metadata()
    if article not in article_metadata:
        abort(404)

    return render_page(
        f"articles/{article}.html",
        "articles",
        article_slug=article,
        navbar="green",
        footer="0",
        footer_two="0",
    )


@app.route("/contact")
def contact():
    return render_page("contact.html", "contact", navbar="green", footer="2rem", footer_two="2rem")
