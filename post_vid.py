import cv2
import os

def create_video(image_paths, video_filename, fps):
    frame = cv2.imread(image_paths[0])
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

    for image in image_paths:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()

def main():
    dir_path_out = os.listdir("out")
    folder_name = input(dir_path_out)

    # Check if folder exists
    if not os.path.exists(folder_name): 
        print("Error: folder does not exist.")
        return

    # Get list of image files in folder
    image_extensions = (".png", ".jpg", ".jpeg")
    image_paths = [os.path.join(folder_name, file) for file in os.listdir(folder_name) if file.endswith(image_extensions)]

    # Sort image paths by filename
    image_paths = sorted(image_paths)

    # Check if there are any images in the folder
    if len(image_paths) == 0:
        print("Error: no image files found in folder.")
        return

    fps = int(input("Enter the frame rate for the video: "))
    video_filename = input("out/vid")

    create_video(image_paths, video_filename, fps)

    print("Video saved as:", video_filename)

if __name__ == "__main__":
    main()
