import requests

class JA3Coll():
    def __init__(self, url="https://ja3er.com/getAllUasJson", output_file="ja3_uas.json"):
        self._url = url
        self._output_file = output_file

    def fetch(self) -> str:
        response = requests.get(self._url, stream = True)

        with open(self._output_file, "wb") as output:
            for chunk in response.iter_content(chunk_size=1024):
                output.write(chunk)

        return self._output_file


if __name__ == "__main__":
    ja3 = JA3Coll()
    ja3.fetch()