# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StackoverflowJobsPipeline(object):
    def process_item(self, item, spider):
        # removing keys from item with empty values
        return {k: v for k, v in item.items() if v}
