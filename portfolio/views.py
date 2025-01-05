from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.templatetags.static import static

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>My Personal Portfolio</title>
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
            rel="stylesheet"
        >
        <style>
            body {
                background-color: #E0E0E0; /* White background */
                color: #000000; /* Black text */
                padding-top: 56px;
            }
            .navbar {
                background-color: #00A6A6; /* Dark grey navbar */
            }
            .navbar-brand, .nav-link {
                color: #ffffff !important; /* White text for navbar items */
            }
            .content-wrapper {
                padding-left: 15px;
                padding-right: 15px;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top w-100">
            <div class="container">
                <a class="navbar-brand" href="/">My Portfolio</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/contact">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container mt-5">
            <div class="row">
                <div class="col-md-8 offset-md-2">
                    <h1 class="display-4 text-center">Welcome to My Portfolio!</h1>
                    <hr class="my-4">
                    <h2 class="text-justify">Introduction</h2>
                    <p class="lead text-justify">My name is Siu Yau Shing (蕭佑丞), also known as Shiloh.</p>
                    <p class="lead text-justify">
                        I am currently studying at The Hong Kong Polytechnic University, pursuing a 
                        <a href="https://www.polyu.edu.hk/dsai/study/ug/bsc-in-fintech-and-ai-62435-fft/" target="_blank">BSc (Hons) in Financial Technology and Artificial Intelligence</a> 
                        with a Minor in Applied Psychology.
                    </p>
                    <p class="lead text-justify">Expected Graduation: September 2027</p>
                    <hr class="my-4">
                    <h2 class="text-justify">Skills</h2>
                    <p class="text-justify"><strong>Programming Languages:</strong> HTML, CSS, Python (Pytorch, Tensorflow, Django), C++, SQL, Java</p>
                    <p class="text-justify"><strong>Office Tools:</strong> Microsoft Office (Word, Excel, PowerPoint, Access)</p>
                    <p class="text-justify"><strong>Languages:</strong> Cantonese (Native), English (Native), Mandarin (Fluent)</p>
                    <p class="text-justify"><strong>Developer Tools:</strong> Docker, Git, Pycharm, VScode, IntelliJ IDEA</p>
                    <div class="text-center">
                        <a href="/projects" class="btn btn-primary mt-3">Go to My Projects</a>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def projects(request):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>My Projects</title>
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
            rel="stylesheet"
        >
        <style>
            body {{
                background-color: #E0E0E0; /* White background */
                color: #000000; /* Black text */
                padding-top: 56px;
            }}
            .navbar {{
                background-color: #00A6A6; /* Dark grey navbar */
            }}
            .navbar-brand, .nav-link {{
                color: #ffffff !important; /* White text for navbar items */
            }}
            .content-wrapper {{
                padding-left: 15px;
                padding-right: 15px;
            }}
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top w-100">
            <div class="container">
                <a class="navbar-brand" href="/">My Portfolio</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/contact">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="content-wrapper container">
            <h1>My Projects</h1>
            <ul>
                <li style="margin-top: 20px;">
                    <h2>Virtual File System in Java</h2>
                    <p>Introduction: This is an in-memory Virtual File System (VFS), named the Comp VFS (CVFS), which is made in Java and utilizes OOP concepts to simulate a file system. The user opens application .java to start the program and use the file system. The application uses the Model-View-Controller Pattern in Designing the CVFS.</p>
                    <img src="{static('images/image1.png')}" alt="Project One" style="width: 400px; height: auto; display: block; margin: 0 auto;">  <br>
                    <a href="https://github.com/J71956/CVFS-Project">Click here to View the Project!</a> 
                </li>
                <li style="margin-top: 20px;">
                    <h2>This Website</h2>
                    <p>This Website is written using Django and Html.</p>
                    <img src="{static('images/image2.jpg')}" alt="Project Two" style="width: 800px; height: auto; display: block; margin: 0 auto;">  <br>
                    <a href="http://example.com/project2">Click here to View the Project!</a>
                </li>
                <!-- Add more projects here -->
            </ul>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html_content)

def contact(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Contact Information</title>
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
            rel="stylesheet"
        >
        <style>
            body {
                background-color: #E0E0E0; /* White background */
                color: #000000; /* Black text */
                padding-top: 56px;
            }
            .navbar {
                background-color: #00A6A6; /* Dark grey navbar */
            }
            .navbar-brand, .nav-link {
                color: #ffffff !important; /* White text for navbar items */
            }
            .content-wrapper {
                padding-left: 15px;
                padding-right: 15px;
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark fixed-top w-100">
            <div class="container">
                <a class="navbar-brand" href="/">My Portfolio</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link" href="/">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/projects">Projects</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/contact">Contact</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <div class="container mt-5">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <div class="card">
                        <div class="card-header text-center">
                            <h2>Contact Information</h2>
                        </div>
                        <div class="card-body">
                            <h3>Get in Touch</h3>
                            <p>If you have any questions or would like to connect, please feel free to reach out through any of the contact methods listed. I look forward to hearing from you!</p>
                            <p><strong>Phone:</strong> +852 97156277</p>
                            <p><strong>Email:</strong> <a href="mailto:shilohsiu0@gmail.com">shilohsiu0@gmail.com</a></p>
                            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/yau-shing-siu-368383225/" target="_blank">Yau Shing Siu</a></p>
                            <p><strong>GitHub:</strong> <a href="https://github.com/J71956" target="_blank">J71956</a></p>
                            <hr>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    return HttpResponse(html_content)