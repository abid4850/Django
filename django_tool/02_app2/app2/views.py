from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Home page of AHN!")

# blogs view
def blogs(request):
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogs | AHN</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: #f5f7fa;
            color: #333;
        }
        header {
            background: #0077b6;
            color: white;
            text-align: center;
            padding: 1.5rem;
        }
        h1 {
            margin: 0;
            font-size: 2rem;
        }
        .container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 1rem;
        }
        .blog-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            padding: 1.5rem;
            transition: transform 0.2s;
        }
        .blog-card:hover {
            transform: translateY(-5px);
        }
        .blog-card h2 {
            margin-top: 0;
            color: #0077b6;
        }
        .blog-card p {
            line-height: 1.6;
        }
        footer {
            text-align: center;
            background: #0077b6;
            color: white;
            padding: 1rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to AHN Blogs</h1>
        <p>Latest thoughts, guides, and ideas</p>
    </header>

    <div class="container">
        <div class="blog-card">
            <h2>🚀 Getting Started with Django</h2>
            <p>Django is a powerful web framework for building secure and scalable applications. 
            In this article, we’ll explore how to start your first Django project step by step.</p>
        </div>

        <div class="blog-card">
            <h2>💡 Online Earning Mastery</h2>
            <p>Discover smart strategies for building online income streams — from freelancing 
            to creating digital products and more.</p>
        </div>

        <div class="blog-card">
            <h2>📊 Data Science & AI</h2>
            <p>Learn how Artificial Intelligence and Data Science are changing the future. 
            Practical tips and project ideas for beginners and professionals alike.</p>
        </div>
    </div>

    <footer>
        <p>© 2025 AHN Blogs | Built with Django</p>
    </footer>
</body>
</html> """

    return HttpResponse(html_content)

