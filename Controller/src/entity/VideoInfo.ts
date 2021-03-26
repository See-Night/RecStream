import { Entity, PrimaryColumn, Column } from "typeorm";

@Entity('VideoInfo_videoinfo')
export class VideoInfo {

    @PrimaryColumn()
    FileName: string;

    @Column()
    Title: string;

    @Column()
    Time: string;

    @Column()
    Date: string;

    @Column()
    LiveURL: string;

    @Column()
    Resolution: string;

    @Column()
    FrameRate: string;

    @Column()
    AudioByteRate: string;

}