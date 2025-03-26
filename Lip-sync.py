def lip_sync(audiofile, videofile, output_name='output'):
  audiofile_path = '../'+audiofile.split("/")[-1]
  videofile_path = '../'+videofile.split("/")[-1]

  %cd /content/Wav2Lip

  # Set up paths and variables for the output file
  output_file_path = '../'+output_name+'.mp4'

  # Delete existing output file before processing, if any
  if os.path.exists(output_file_path):
      os.remove(output_file_path)
  print('AUDIO FILE: ',audiofile_path)
  print('VIDEO FILE: ',videofile_path)
  print('OUTPUT FILE: ',output_file_path)

  pad_top =  0
  pad_bottom =  10
  pad_left =  0
  pad_right =  0
  rescaleFactor =  1
  nosmooth = True

  # Model selection:
  use_hd_model = True
  checkpoint_path = 'checkpoints/wav2lip.pth' if not use_hd_model else 'checkpoints/wav2lip_gan.pth'

  if nosmooth == False:
    !python inference.py --checkpoint_path $checkpoint_path --face $videofile_path --audio $audiofile_path --outfile $output_file_path --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor
  else:
    !python inference.py --checkpoint_path $checkpoint_path --face $videofile_path --audio $audiofile_path --outfile $output_file_path --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor --nosmooth

  #Preview output video
  if os.path.exists(output_file_path):
      clear_output()
      # print("Final Video Preview")
      print("Download this video from", output_file_path)
      # showVideo(output_file_path)
      %cd ..
  else:
      print("Processing failed. Output video not found.")
      %cd ..