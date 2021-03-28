from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Settings"),
			"items": [
				{
					"label": "WooETMS",
					"type": "doctype",
					"name": "WooCommerce Config"
				},
				{
					"label": "WooETMS Logs",
					"type": "doctype",
					"name": "woocommerce Log"
				},
			
			]
		}
	]
