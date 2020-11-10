from app import app


@app.template_filter('localize')
def cdn_localize(text):
    return app.config['S3_BUCKET_URL'].format(text.split('/')[-1])
