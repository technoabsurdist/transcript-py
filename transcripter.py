import sieve
from google.cloud import storage
import datetime
import youtube_dl
import uuid

# Generate a UUID version 4
uuid_v4 = uuid.uuid4()

storage_client = storage.Client.from_service_account_json('./vivid-motif-402201-eadcd1112018.json')

async def upload_to_cloud_storage(file_content, bucket_name, file_name) -> str:
    try:
        storage_client = storage.Client()

        bucket = storage_client.get_bucket(bucket_name)

        blob = bucket.blob(file_name)

        blob.content_type = 'video/mp3' # Change back to mp4 if not working

        blob.upload_from_string(file_content)

        url = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(hours=1),  # Expires in 1 hour
            method="GET",
        )

        return url

    except Exception as error:
        print('Error uploading to Google Cloud Storage:', error)
        raise Exception('Unable to upload file to Cloud Storage')


def video_transcript_analyzer(url, max_summary_length=10, max_title_length=10, num_tags=5, generate_chapters=True):

    file = sieve.File(url=url)

    transcriber = sieve.function.get("sieve/video_transcript_analyzer")
    output = transcriber.run(file, max_summary_length, max_title_length, num_tags, generate_chapters)

    for output_object in output:
        print(output_object)

    return output

def download_audio(link):
    output_file_name = "output.mp3"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file_name,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def transcribe(url: str):
    # Download video
    audio = download_audio(url) 

    # Process Video 
    bucket_name = 'sieve-transcription'
    file_name = f"output-{uuid.uuid4()}.mp4"
    video_bucket_url = upload_to_cloud_storage(audio, bucket_name, file_name)
    print("Video Bucket URL", video_bucket_url)

    # Get Transcript and other data
    result = video_transcript_analyzer(video_bucket_url)
    print(result)
    return result


