---
permalink: /publications/
title: "Publications"
author_profile: true
---

{% capture publications_source %}{% include_relative includes/pub_short.md %}{% endcapture %}
{% include publications-list.html source=publications_source %}
