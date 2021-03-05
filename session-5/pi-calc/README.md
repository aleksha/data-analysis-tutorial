# Calculation of pi number

```bash
cat *.png | ffmpeg -f image2pipe -r 2 -i - -vcodec libx264 out.mp4
ffmpeg -i out.mp4 -pix_fmt rgb24 -s qcif  new.gif
```