def transFormat(input_dir,input_file, output_dir, input_format, out_format):
    """
    转换音频编码或封装格式
    Args:
        output_dir:同名输出的文件夹
    
    不需要编码格式转换的直接用copy，需要编码格式转换的注意修改编码器
    """
    indeed_format = input_dir.split(".")[-1]
    base_file_name = input_dir.split(".")[0]
    if input_format != indeed_format:
      raise Exception("编码格式不匹配")
    cmd = [
        "ffmpeg",
        "-i", os.path.join(input_dir,input_file),
        "-c:a", "copy", # 不换编码，只拷贝
        
        # "-c:a", "libmp3lame",  # 使用 libmp3lame 编码器
        # "-q:a", "2",  # 设置 MP3 的质量，取值范围为 0-9，值越小质量越高，默认值为 4

        # "-c:a", "libvorbis", # ogg的编码器

        # "-c:a", "aac",  #aac
        # "-strict", "experimental",

        # "-c:a", "amr_nb", # amr
        # "-ar", "8000",
        os.path.join(output_dir,base_file_name+"."+out_format)
    ]

    subprocess.run(cmd, check=True)

def show_msg(file):
    '''
    展示文件信息

    Args:
        file: 需要查看的文件路径

    Returns:

    '''
    cmd = [
        "ffmpeg",
        "-i", file,
        "-vn" # 只包含音频流，不含视频流
    ]
    subprocess.run(cmd, check=True)

def clip_audio(input_file,output_file, start, end):
    """
    根据开始时间和结束时间切分音频并导出新文件

    Args:
        input_file: 源音频文件路径
        output_file: 导出音频文件路径
        start: 开始时间 eg.start 65.106689, end 335.335000
        end: 结束时间

    Returns:

    """

    cmd = [
        "ffmpeg",
        "-ss", start,
        "-to", end,
        "-i",input_file,
        "-c:a","pcm_s24le",#保持编码格式
        output_file
    ]
    subprocess.run(cmd, check=True)
