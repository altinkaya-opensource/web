/** @odoo-module **/
import {ProgressBarField} from "@web/views/fields/progress_bar/progress_bar_field";
import {registry} from "@web/core/registry";

export class ProgressBarFieldColor extends ProgressBarField {
    setup() {
        super.setup();
    }
}
ProgressBarFieldColor.template = "web_widget_progressbar_color.ProgressBarFieldColor";
registry.category("fields").add("progressbar_color", ProgressBarFieldColor);
