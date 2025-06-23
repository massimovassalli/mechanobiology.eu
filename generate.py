from pathlib import Path

# Page names and titles
pages = {
    "index.html": "European Society for MechanoBiology (ESMB)",
    "manifest.html": "ESMB Manifest",
    "stories.html": "Mechanobiology Stories",
    "editorial.html": "Editorial Initiatives",
    "events.html": "Events",
    "education.html": "Education and Training",
    "structure.html": "Structure"
}

body = {
    "index.html": '''
    <p class="lead">
      The survey results are now available! More than 200 scientists from all over Europe have shared their thoughts and ideas on how to shape 
      the future of the mechanobiology community in Europe through the establishment of a scientific society. A general support for the initiative has been gathered 
      since December 2024, highlighting the most relevant actions to support the consolidation of mechanobiology across Europe.
    </p>

    <p class="lead">
        The survey has identified 5 main activities that the community would like to help with, to consolidate the ESMB and get to its formal foundation. These correspond 
        to the main items of the navigation menu, and will be the focus of the next steps of the ESMB initiative. The content will be uploaded as soon as available. 
      </p>

    <p class="lead">
      If you want to contribute to shaping the future of the mechanobiology community in Europe, we invite you to subscribe to 
      the mailing list, to get updates on the next steps. You can also directly write to us, to share ideas, questions and suggestions.
      </p>

    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      <a type="button" href="assets/survey.pdf" target="_blank" class="btn btn-outline-secondary btn-lg px-4">Download the survey results</a>
      <a type="button" href="https://www.freelists.org/list/mechanobiology" target="_blank" class="btn btn-outline-primary btn-lg px-4 gap-3">Subscribe the mailing list</button>
      <a type="button" href="mailto:ideas@mechanobiology.eu" class="btn btn-outline-secondary btn-lg px-4">Contact us</a>
    </div>''',
}

# Template content for subpages
template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} - ESMB</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" />
  <link rel="stylesheet" href="assets/styles.css" />
  <link rel="apple-touch-icon" sizes="180x180" href="assets/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16x16.png">
  <link rel="manifest" href="assets/site.webmanifest">
  <link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet">
</head>
<body>
  <header class="container py-3">
    <div class="d-flex flex-wrap align-items-center justify-content-between">
      <img src="assets/logo.png" alt="ESMB Logo" class="logo" height="80">
      <ul class="nav nav-pills">
        <li class="nav-item"><a href="index.html" class="nav-link">Home</a></li>
        <li class="nav-item"><a href="manifest.html" class="nav-link">ESMB Manifest</a></li>
        <li class="nav-item"><a href="stories.html" class="nav-link">Mechanobiology Stories</a></li>
        <li class="nav-item"><a href="editorial.html" class="nav-link">Editorial Initiatives</a></li>
        <li class="nav-item"><a href="events.html" class="nav-link">Events</a></li>
        <li class="nav-item"><a href="education.html" class="nav-link">Education & Training</a></li>
        <li class="nav-item"><a href="structure.html" class="nav-link">Structure</a></li>
      </ul>
    </div>
  </header>

  <main class="container handwritten mt-5">
    <h1 class="display-4">{title}</h1>
    {body}
  </main>

  <footer class="container mt-5 py-3 border-top text-center">
    <p>Website: <a href="https://www.mechanobiology.eu">www.mechanobiology.eu</a> | Contact: <a href="mailto:ideas@mechanobiology.eu">ideas@mechanobiology.eu</a></p>
  </footer>
</body>
</html>
"""

# Write each HTML page to file
output_dir = Path("./")
output_dir.mkdir(parents=True, exist_ok=True)

for filename, title in pages.items():
    if filename in body.keys():
        content = body[filename]
    else:
        content = "<p class='lead'>[Content coming soon]</p>"
    (output_dir / filename).write_text(template.format(title=title,body=content))

output_dir.mkdir(exist_ok=True)
output_dir_path = str(output_dir)
output_dir_path
