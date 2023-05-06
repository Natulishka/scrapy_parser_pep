import csv
from datetime import datetime

from scrapy.exceptions import DropItem

from .constants import BASE_DIR, DATETIME_FORMAT, EXPECTED_STATUS


class PepParsePipeline:
    '''Обработка объектов Items.'''

    def open_spider(self, spider):
        '''Операции, вполняемые при старте работы паука.'''
        self.amount_statuses = {}

    def process_item(self, item, spider):
        '''Обрабатывает объекты Items.'''
        if item['status'] not in EXPECTED_STATUS:
            raise DropItem(f'''
            Обнаружен неизвестный статус у PEP № {item['number']}:
            {item['status']}
            ''')
        self.amount_statuses[item['status']] = self.amount_statuses.get(
            item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        '''Операции, вполняемые при окончании работы паука.'''
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8', newline='') as csvfile:
            summarywriter = csv.writer(csvfile)
            summarywriter.writerow(['Статус', 'Количество'])
            for status, amount in sorted(self.amount_statuses.items()):
                summarywriter.writerow([status, amount])
            summarywriter.writerow(['Total',
                                    sum(self.amount_statuses.values())])
