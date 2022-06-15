import frappe
from frappe import _
from frappe.utils import get_link_to_form

def update_task_template_detail_based_on_project_template(self,method):
    for task in self.tasks:
        msg=None
        start_cf=None
        task_details = frappe.get_doc("Task", task.task)
        if task_details.start != task.start_cf:
            frappe.db.set_value('Task', task.task, 'start', task.start_cf)
            msg=_('Task {0} , Begin On (Days) is changed from {1} to {2}'.
            format(get_link_to_form('Task',task.task),task_details.start,frappe.bold(task.start_cf)))
            start_cf=task.start_cf
        if task_details.duration != task.duration_cf:
            frappe.db.set_value('Task', task.task, 'duration', task.duration_cf)
            if not start_cf:
                msg=_('Task {0} , Duration (Days) is changed from {1} to {2}'.
                format(get_link_to_form('Task',task.task),task_details.duration,frappe.bold(task.duration_cf)))
            else:
                msg=msg+_('<br> Duration (Days) is changed from {0} to {1}'.
                format(task_details.duration,frappe.bold(task.duration_cf)))
        if msg:
            frappe.msgprint(msg, indicator="orange", alert=True)