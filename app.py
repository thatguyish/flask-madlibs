from flask import Flask, request, render_template
from stories import story as s
app= Flask('__name__')

@app.route('/')
def story_begining():
    story_v = s.prompts

    return render_template('base.html', s_v=story_v)

@app.route('/story')
def story():

    full = s.generate(request.args)
    return render_template('story.html',full=full)
