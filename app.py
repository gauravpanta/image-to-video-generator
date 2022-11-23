import av
import os
import cv2
import traceback

def create_video(path, fps, output):
    vid = av.open(output, "w")
    vs = vid.add_stream("h264", fps)

    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            try:
                img = cv2.imread(filepath, 1)
                for i in range(0,fps):
                    new_frame = av.VideoFrame.from_ndarray(img, format="rgb24")
                    new_frame.pts = None
                    vid.mux(vs.encode(new_frame))
            except Exception as e:
                print(e)
                traceback.print_exc()
    vid.close()

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True)
    parser.add_argument("-f", "--fps", required=False, default=30)
    parser.add_argument("-o", "--output", required=False, default="out.mp4")
    args = parser.parse_args()
    
    print("PATH", args.path)
    print("FPS", args.fps)
    print("Output File", args.output)
    create_video(args.path, int(args.fps), args.output)