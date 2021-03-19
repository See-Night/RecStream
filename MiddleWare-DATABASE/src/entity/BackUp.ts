import { Entity, PrimaryGeneratedColumn, Column, PrimaryColumn } from "typeorm";

@Entity('BackUp')
export class BackUp {

    @PrimaryColumn()
    Date: string;

    @Column()
    Path: string;

}
