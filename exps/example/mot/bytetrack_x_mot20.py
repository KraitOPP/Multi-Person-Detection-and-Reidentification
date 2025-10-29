from yolox.exp import Exp as MyExp

class Exp(MyExp):
    def __init__(self):
        super().__init__()

        # single class (person)
        self.num_classes = 1

        # model scale (ByteTrack X)
        self.depth = 1.33
        self.width = 1.25

        # input image size
        self.input_size = (608, 1088)
        self.test_size = (608, 1088)

        # confidence & NMS thresholds
        self.test_conf = 0.001
        self.nmsthre = 0.7

        # tracking parameters
        self.track_high_thresh = 0.6
        self.track_low_thresh = 0.1
        self.new_track_thresh = 0.7
        self.match_thresh = 0.8
        self.proximity_thresh = 0.5
        self.appearance_thresh = 0.25
        self.track_buffer = 30

        # others
        self.fp16 = True
        self.mot20 = True

    def get_model(self):
        from yolox.models import YOLOX, YOLOPAFPN, YOLOXHead
        if getattr(self, "model", None) is None:
            in_channels = [256, 512, 1024]
            backbone = YOLOPAFPN(self.depth, self.width, in_channels=in_channels)
            head = YOLOXHead(self.num_classes, self.width, in_channels=in_channels)
            self.model = YOLOX(backbone, head)
        return self.model
