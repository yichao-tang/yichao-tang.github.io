---
permalink: /zh/publications/
title: "学术论文"
author_profile: true
lang: zh
translation_key: publications
---

{% capture publications_source %}{% include_relative includes/pub_short.md %}{% endcapture %}
{% include publications-list.html source=publications_source %}
