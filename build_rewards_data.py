from lxml import html
from json import dump
from os import remove
class BuildRewardsData:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = "/Users/usuario/Downloads/" + self.file_name
        self.html_tree = self.build_html_tree()

    def build_html_tree(self):
      html_tree = ""
      with open(self.file_path, 'r', encoding='utf-8') as file:
          content = file.read()
          html_tree = html.fromstring(content)

      return html_tree

    def build_json(self):
      daily_set_elements = self.html_tree.xpath("//div[contains(@class, 'm-card-group')]")[0].xpath(".//mee-card")
      more_activities_element = self.html_tree.xpath("//div[contains(@class, 'm-card-group')]")[2].xpath(".//mee-card")

      return {
         'name': self.html_tree.xpath("//h1[@persona-name]/text()")[0].strip(),
         'level': self.html_tree.xpath("//p[contains(@class, 'level')]/text()")[0].strip(),
         'available_points': self.html_tree.xpath("//p[contains(@class, 'pointsValue')]")[0].xpath(".//span/text()")[0].strip(),
         'todays_points': self.html_tree.xpath("//p[contains(@class, 'pointsValue')]")[2].xpath(".//span/text()")[0].strip(),
         'streak_count': self.html_tree.xpath("//p[contains(@class, 'pointsValue')]")[3].xpath(".//span/text()")[0].strip(),
         'daily_set': self.build_json_sub_section(daily_set_elements),
         'more_activities': self.build_json_sub_section(more_activities_element)
      }

    def build_json_sub_section(self, elements):
      sub_section = []

      for index, element in enumerate(elements):
        card_points = element.xpath(".//div[contains(@class, 'points')]/div/span")
# card_points[1].xpath(".//span[contains(@class='mee-icon-AddMedium'])")
        if not card_points:
          sub_section.append(
            {
              'card_number': index + 1,
              'points?': False,
              'points': 0,
              'available_points': False
            }
          )
        else:
          sub_section.append(
            {
              'card_number': index + 1,
              'points?': True,
              'points': card_points[1].xpath(".//text()"),
              'available_points': card_points[0].attrib.get("class", "") == 'mee-icon mee-icon-AddMedium',
            }
          )

      return sub_section

    def build_reward_data_file(self, data):
      with open('rewards_data.json', "w") as json_file:
        dump(data, json_file, indent=4)

    def delete_file_downloaded(self):
      remove(self.file_path)

    def call(self):
      data = self.build_json()
      self.build_reward_data_file(data)
      self.delete_file_downloaded()

      return data
