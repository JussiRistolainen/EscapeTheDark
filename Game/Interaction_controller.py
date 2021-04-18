

def clicked(icon, time_count, item_methods, pos):
    if icon == 1 and time_count.get_logs() > 0:
        item_methods.create_log_with_pos(pos)
        time_count.remove_item("Log")
    if icon == 2 and time_count.get_matches() > 0:
        item_methods.check_for_log(pos)
        time_count.remove_item("match")
    if icon == 0:
        item_methods.lift_item(time_count, pos)