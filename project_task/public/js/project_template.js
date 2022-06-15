frappe.ui.form.on('Project Template Task', {
	task: function (frm, cdt, cdn) {
		var row = locals[cdt][cdn];
        frappe.db.get_value('Task', row.task, ['start', 'duration'])
        .then(r => {
            let values = r.message;
            if (row.start_cf==undefined || row.start_cf=='') {
                row.start_cf=values.start
            }
            if (row.duration_cf==undefined || row.duration_cf=='') {
                row.duration_cf=values.duration
            }
            refresh_field("tasks");
        })
	}
});