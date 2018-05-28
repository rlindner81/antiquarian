@ECHO OFF
SETLOCAL enableDelayedExpansion
FOR /L %%i IN (13,13,13) DO (
	SET j=0%%i
	SET j=!j:~-2!
	ECHO processing volume !j!
	convert -flatten cover-vol-!j!.xcf cover-vol-!j!.jpg
	convert -flatten cover-vol-!j!.jpg -resize 200 thumb-vol-!j!.jpg
	convert -flatten cover-vol-!j!-comments.xcf cover-vol-!j!-comments.jpg
	convert -flatten cover-vol-!j!-comments.jpg -resize 200 thumb-vol-!j!-comments.jpg
)
ENDLOCAL