import requests
from user_agents import parse

class JA3Coll():
    def __init__(self, url="https://ja3er.com/getAllUasJson", output_file="ja3_uas.json"):
        self._url = url
        self._output_file = output_file

    def fetch(self) -> str:
        print(f"Fetching File...")
        response = requests.get(self._url, stream = True)

        with open(self._output_file, "wb") as output:
            for chunk in response.iter_content(chunk_size=1024):
                output.write(chunk)

        print(f"File Fetched..")
        return self._output_file

    @staticmethod
    def parse_user_agent(row) -> dict:       
        user_agent = parse(row['User-Agent'])
        row['Browser_Family'] = user_agent.browser.family
        row['OS_Family'] = user_agent.os.family
        row['OS_Version'] = user_agent.os.version
        row['Device'] = user_agent.device.model
        return row



    def load_to_pd(self, input_file: str = "ja3_uas.json"):
        print(f"Loading File...")
        import pandas as pd
        df = pd.read_json(input_file)
        df = df.apply(self.parse_user_agent, axis=1)
        print(f"File Loaded...")
        return df


if __name__ == "__main__":
    ja3 = JA3Coll()
    # ja3.fetch()
    df = ja3.load_to_pd()