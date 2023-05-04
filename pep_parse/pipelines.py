from datetime import datetime

from scrapy.exceptions import DropItem

from .constants import BASE_DIR, DATETIME_FORMAT, EXPECTED_STATUS


class PepParsePipeline:
    '''Обработка объектов Items.'''

    def open_spider(self, spider):
        '''Операции, вполняемые при старте работы паука.'''
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        self.file_path = results_dir / file_name
        self.amount_statuses = {}

    def process_item(self, item, spider):
        '''Обрабатывает объекты Items.'''
        self.amount_statuses[item['status']] = self.amount_statuses.get(
            item['status'], 0) + 1
        if item['status'] not in EXPECTED_STATUS:
            raise DropItem(f'''
            Обнаружен неизвестный статус у PEP № {item['number']}:
            {item['status']}
            ''')
        return item

    def close_spider(self, spider):
        '''Операции, вполняемые при окончании работы паука.'''
        with open(self.file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for status, amount in sorted(self.amount_statuses.items()):
                f.write(f'{status},{amount}\n')
            f.write(f'Total,{sum(self.amount_statuses.values())}')
