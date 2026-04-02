from django.shortcuts import render


def home(request):
    context = {
        "name": "Pranali Parasharam Jadhav",
        "short_name": "PJ",
        "role": "Open to Work",
        "hero_title": "Future IT professional with a passion for smart solutions.",
        "tagline": "MCA student passionate about Django, Python, frontend design, and building responsive full stack projects.",
        "about_text": "I am an MCA Student with a strong interest in Full Stack Development and building practical digital solutions. I enjoy learning new technologies and applying my academic knowledge to real-world projects. Eager to contribute to the growth of an organization through dedication and continuous improvement. I am committed to enhancing my technical skills while gaining valuable professional experience. My goal is to grow personally and professionally while supporting organizational success.",
        "email": "jadhavpranali7411@gmail.com",
        "phone": "+91 7411271288",
        "location": "Belagavi, Karnataka, India",
        "github": "https://github.com/Pranali2002-Jadhav",
        "linkedin": "https://www.linkedin.com/in/pranali-jadhav-360298298",
        "resume_link": "#",

        "skills": {
            "Frontend": [
                {"name": "HTML"},
                {"name": "CSS"},
                {"name": "JavaScript"},
                {"name": "Bootstrap"},
            ],
            "Backend": [
                {"name": "Python"},
                {"name": "Django"},
                {"name": "Java"},
                {"name": "PHP"},
                {"name": "C#"},
            ],
            "Database": [
                {"name": "MongoDB"},
                {"name": "MySQL"},
            ],
            "Tools": [
                {"name": "GitHub"},
                {"name": "Figma"},
                {"name": "VS Code"},
            ]
        },

        "projects": [
            {
                "title": "Online Leave Management System ",
                "description": "Developed a web-based mini project using ASP.NET ,C#,SQL Server to automate leave  Application and approval processes.  ",
                "tech": "ASP.NET,C#,SQL Server",
                "link": "#"
            },
            {
                "title": "Library Management System ",
                "description": "Develop a Library Management System to Implementing CRUD Operations (Create, Read,  Update, Delete) Using PHP and MongoDB. ",
                "tech": "PHP,MongoDB,HTML,CSS",
                "link": "#"
            },
            {
                "title": "Online Blogging Platform Sytem",
                "description": "Developed a web-based application using Django framework that enables users to create,  publish and manage blog posts in interactive and secure environment.  ",
                "tech": "Django, Python, SQLite",
                "link": "#"
            }
        ]
    }
    return render(request, "portfolio/index.html", context)