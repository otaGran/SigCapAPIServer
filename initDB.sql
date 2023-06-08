-- Drop the table if it exists
DROP TABLE IF EXISTS "SigCapDetails";

create table "SigCapDetails"
(
    uid                     SERIAL PRIMARY KEY,
    "deviceID"              text,
    "operatorID"            text,
    "batchUUID"             text,
    "recordTimeStamp"       timestamp(3),
    azimuth                 numeric,
    pitch                   numeric,
    roll                    numeric,
    longitude               numeric,
    latitude                numeric,
    altitude                numeric,
    "mRegistered"           bool,
    "mTimeStamp"            bigint,
    "mCellConnectionStatus" integer,
    "mCi"                   integer,
    "mPci"                  integer,
    "mEarfcn"               integer,
    "mBandwidth"            integer,
    "mMcc"                  text,
    "mMnc"                  text,
    rssi                    integer,
    rsrp                    integer,
    rsrq                    integer,
    rssnr                   integer,
    cqi                     integer,
    "timingInAdvanced"      integer
);
