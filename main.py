from utils import read_video,save_video
from trackers import Tracker

def main():

    #read video
    #D:\YOLO_Sports_Analysis\input_video\08fd33_4.mp4
    #input_video\08fd33_4.mp4
# • \ → Windows path separator (e.g., D:\folder\file.py) in Microsoft Windows

# • / → Linux/macOS path separator in Linux and macOS

# • In Python, / works on all systems, so it is usually preferred.
    video_frames=read_video("input_video/08fd33_4.mp4")

    #initialize tracker
    tracker=Tracker('models/best.pt')
    tracks=tracker.get_object_tracks(video_frames,
                                    read_from_stub=True,
                                    stub_path='stubs/track_stubs.pkl')
    

    #Draw Output
    output_video_frames=tracker.draw_annotations(video_frames,tracks)

    #save video
    save_video(output_video_frames,'output_video/output_video.avi')
if __name__=='__main__':
    main()    