# (x1, y1): The top-left corner of the bounding box.
# (x2, y2): The bottom-right corner of the bounding box


def get_center_of_bbox(bbox):
    x1,y1,x2,y2=bbox
    return int((x1+x2)/2),int((y1+y2)/2)
def get_bbox_width(bbox):
    return bbox[2]-bbox[0]