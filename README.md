# Django�̊�{�ۑ�
Django�̊�{�Z�p�̏K���m�F�̂��߂̉ۑ�ł�

DB�̒��g���Q�Ƃ��邽�߁ADB�N���C�A���g���C���X�g�[�����Ă��������B
�����L�͎Q�l�̂��߁A���D����DB�N���C�A���g�ō\���܂���
�Q�l�Fhttps://forest.watch.impress.co.jp/library/software/heidisql/

## �P
�D���Ȗ��O�̃A�v���P�[�V�������쐬���A�uhello world�v��
�Œ�ŕ\������Web�y�[�W���쐬���Ă��������B

## �Q
template���g���A�����T�C�h���j���[�̃y�[�W���Q�쐬���Ă�������
�T�C�h���j���[�̍\���́A�ȉ��̒ʂ�Ƃ��Ă��������B
�S�ł̐n
�@|_ �L�����N�^�[�o�^
�@|_ �L�����N�^�[�ꗗ

## �R
�T�C�h���j���[�́u�L�����N�^�[�o�^�v���烊���N�������y�[�W��
���̓t�H�[�����쐬���Ă�������
���͍��ڂ͈ȉ��̒ʂ�ł��B

���O�i�e�L�X�g�j
���ʁi�I�����j
�����i�e�L�X�g�j

## �S
model���g���A�S�ł̃L�����N�^�[�����i�[����model���쐬���Ă��������B
migrate����DB�Ƀe�[�u�����ł��邱�Ƃ��m�F���Ă��������B

## �T
�ۑ�R�ō�����t�H�[����model��A�g�����āA�t�H�[���œo�^�������e��DB�ɋL�^�����悤�ɂ��Ă��������B

## �U
DB�ɓo�^���ꂽ�S�ł̃L�����N�^�[���u�L�����N�^�[�ꗗ�v���烊�X�g�\���ł��悤�ɂ��Ă�������

## �V
GCP���g�p���ĂU�܂łɍ쐬����Django�v���W�F�N�g���f�v���C���Ă�������<BR>
�Q�l�Fhttps://hack.nikkei.com/blog/cloud_run_blog/  <BR>
�ꕔ�ύX���K�v�ł��B<BR>
  
�EDocker�t�@�C���͈ȉ��̂悤�ɂ���<BR>
�T�C�g�L�ځFCMD gunicorn config.wsgi -b 0.0.0.0:$PORT<BR>
�C���FCMD gunicorn <�v���W�F�N�g��>.wsgi -b 0.0.0.0:$PORT<BR>
�Esettings��allowshost�Ɏ��g��GCP�̃z�X�g����ǉ�<BR>
�E�f�v���C�R�}���h��--platform managed ��t�^<BR>
gcloud beta run deploy <�T�[�r�X��> --image gcr.io/<�v���W�F�N�gID>/<�C���[�W��> --region us-central1 --platform managed

