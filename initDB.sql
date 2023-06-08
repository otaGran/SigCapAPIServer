-- Drop the table if it exists
DROP TABLE IF EXISTS "SigCapDetails";

create table public."SigCapDetails"
(
    uid                     serial
        primary key,
    "deviceID"              text,
    "operatorID"            text,
    "batchUUID"             text,
    azimuth                 numeric,
    longitude               numeric,
    latitude                numeric,
    altitude                numeric,
    "mRegistered"           boolean,
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
    "timingInAdvanced"      integer,
    pitch                   numeric,
    roll                    numeric,
    "recordTimeStamp"       timestamp(3),
    "magAccuracy"           integer,
    "gpsHorAccuracy"        numeric,
    valid                   text,
    "validTime"             text,
    "validComment"          text
);

alter table public."SigCapDetails"
    owner to postgres;


