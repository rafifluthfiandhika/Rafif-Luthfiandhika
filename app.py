from wsgiref.simple_server import make_server
import falcon


class HomeResource:

  def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
    # 1. Bungkus teks dengan tag HTML <h1>
    resp.text = """
    <h1>HELLO WORD</h1>
    <h2>#PBW3B1PBL0101</h2>
    <p>RAFIF LUTHFIANDHIKA</p>
    <p>251080200014</p>
    <p>Framework > Python [9] > Falcon</p>
    <p>TIME : 2026 - 09 - 24 (10.30)</p>"""

    # 2. Ubah tipe konten menjadi HTML
    resp.content_type = falcon.MEDIA_HTML


class QuoteResource:

  def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
    resp.media = {
        'quote': (
            "I've always been more interested in the future than in the"
            ' past.'
        ),
        'author': 'Grace Hopper',
    }


app = falcon.App()

app.add_route('/', HomeResource())
app.add_route('/quote', QuoteResource())

if __name__ == '__main__':
  with make_server('127.0.0.1', 8002, app) as httpd:
    print('Server berjalan di http://localhost:8002')
    httpd.serve_forever()
