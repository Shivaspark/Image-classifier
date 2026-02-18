from bing_image_downloader import downloader

# Downloading images using bing-image-downloader which is currently more reliable
# than google image scrapers.
downloader.download(
    "Sachin", 
    limit=10, 
    output_dir='Dataset/test', 
    adult_filter_off=True, 
    force_replace=False, 
    timeout=60, 
    verbose=True
)