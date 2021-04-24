

def clicked(icon, time_count, item_methods, pos, character):
    if character.get_distance_from_position(pos) < 100:
        if character.return_item_name() == "Lantern":
            item_methods.place_lantern(pos, character.get_item())
        elif icon == 1 and time_count.get_logs() > 0:
            item_methods.create_log_with_pos(pos)
            time_count.remove_item("Log")
        elif icon == 2 and time_count.get_matches() > 0:
            item_methods.check_for_log(pos)
            time_count.remove_item("match")
        elif icon == 0:
            item_methods.lift_lantern(pos)
            item_methods.lift_item(time_count, pos)
        elif icon == 4 and time_count.get_oil() > 0:
            item_methods.check_lantern(pos, time_count)
    if icon == 3 and time_count.get_logs() > 0:
        item_methods.create_torch()
        time_count.remove_item("match")
        time_count.remove_item("Log")

