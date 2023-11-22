
<div align="center">
  <br />
  <br />
  <img src="yb.png" height="100" width="100">
  <br />
  <br />
  <h3>Transcript.ai (Python Backend Version)</h3>
  <h4>Transcript Youtube links along with AI-generated title, summary, chapters, and tags.</h4>
  <h5>Powered by <a href="https://www.sievedata.com/">Sieve</a>
</div>

## Live Demo with Frontend
[Youtube Transcript Live App](https://transcript-fe.vercel.app/)

## Original TypeScript Express Version
[Express Version](https://github.com/technoabsurdist/transcript.ai)

## Overview
This is the Python version of the backend service for Youtube Transcript AI. An application to develop detailed
transcripts in over 50 languages, enhanced with AI-created titles, chapter divisions,
concise summaries, and relevant tags. It is built using Node.js with Express and is designed
with a very simplistic model. <br /> <br /> **Simply one endpoint `/submit` that takes in a raw youtube link and interacts with the Sieve Data
API to create the full transcription alongside the specified features in downloadable PDF form.**
<br /> 
<br />

## To-Dos
* **Reduce latency** / **Increase Processing Speed**. Videos take *way too long to transcript*. I'm not sure what's the biggest bottleneck 
* **Modularize endpoints while maintaining speed** 
* ... 

## Setup and Installation


- Clone the repository.
- Run npm install to install dependencies.
- Install `requirements.txt` with `pip install -r requirements.txt`
- Run flask server with `python app.py`
- Send a request to the API endpoint `/submit`

## API Endpoint
POST `/submit` - Submit a link for transcription and title retrieval. <br />
Body: `{ "link": "URL" }` <br /> 
Output: `{ text, summary, title, tags, chapters }`

## Usage

To interact with the server, send HTTP requests to the respective endpoints with the required data.

## Error Handling

The server provides basic error handling for failed requests or internal errors.

## Dependencies
express
dotenv
body-parser
cors
axios

## Contributing

This project is *very early stages*, so contributions are very welcome! Please ensure to follow the project's code style and contribution guidelines.

Shoot me an email with questions or if you get stuck at any part andere.emi@gmail.com