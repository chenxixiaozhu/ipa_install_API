from flask import Flask,send_file,render_template

app = Flask(__name__)


@app.route('/Load/<string:url>')
def hello_world(url):  # put application's code here
    plist_file=open("apps.plist","a+")
    plist_file.write("""<plist version="1.0">
<dict>
<key>items</key>
<array>
<dict>
<key>assets</key>
<array>
<dict>
<key>kind</key>
<string>software-package</string>
<key>url</key>
<string>
<![CDATA["""+url+"""]]>
</string>
</dict>
</array>
<key>metadata</key>
<dict>
<key>bundle-identifier</key>
<string>com.tencent.xin1</string>
<key>bundle-version</key>
<string>4.4</string>
<key>kind</key>
<string>software</string>
<key>title</key>
<string>apps</string>
</dict>
</dict>
</array>
</dict>
</plist>""")
    plist_file.close()
    return send_file("apps.plist", mimetype='application/plist')
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

