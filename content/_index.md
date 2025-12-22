+++
title = "Home"
sort_by = "weight"

[extra]
header = {title = "Mihir Vinay Kulkarni", img = "img/main.webp", img_alt = "Mihir Vinay Kulkarni" }
projects_path = "projects/_index.md"
max_projects = 3
show_projects_first = false
social_media_card = "index.jpg"
+++

I am a Researcher at the [Norwegian University of Science and Technology (NTNU)](https://www.ntnu.no) in the Department of Engineering Cybernetics. My research focuses on **aerial robotics**, **reinforcement learning**, and **autonomous navigation** in complex, GPS-denied environments.

I recently completed my Ph.D. in Engineering Cybernetics at NTNU, where I worked on enabling resilient autonomy for robotic systems. My work bridges the gap between theoretical robust control and practical, real-world deployment on limited-compute platforms.

{% menu_container() %}
    {{ menu_item(title="Publications", url="/publications/", icon="book", text="See my research papers and journals.") }}
    {{ menu_item(title="Experience", url="/experience/", icon="briefcase", text="My academic journey.") }}
    {{ menu_item(title="Projects", url="/projects/", icon="rocket", text="Gallery of my work.") }}
    {{ menu_item(title="Download CV", url="/files/cv.pdf", icon="download", text="Get a copy of my CV.") }}
{% end %}

---

### Technical Expertise

{{ skills_grid() }}
