class ArMarkerPoint:
    def __init__(self, ar_marker_id, corner_points):
        self.ar_marker_id = ar_marker_id
        self.corner_points = corner_points.tolist()
        self.left_top = corner_points[0].tolist()
        self.right_top = corner_points[1].tolist()
        self.right_bottom = corner_points[2].tolist()
        self.left_bottom = corner_points[3].tolist()

    def __lt__(self, other):
        return self.left_top < other.left_top

    def show(self):
        return f'ar_marker_id: {self.ar_marker_id}, corner_points: {self._corner_points_formatter()}\n'

    def _corner_points_formatter(self):
        return [self.left_top, self.right_top, self.right_bottom, self.left_bottom]
