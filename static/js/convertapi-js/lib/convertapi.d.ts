declare namespace ConvertApi {
    interface Credentials {
        secret: string;
        apiKey: string;
        token: string;
    }
    export function auth(credentials: Credentials, host?: string): ConvertApi;
    class ConvertApi {
        readonly credentials: Credentials;
        readonly host: string;
        constructor(credentials: Credentials, host?: string);
        createParams(init?: IParamInit[]): Params;
        convert(fromFormat: string, toFormat: string, params: IParams): Promise<Result>;
    }
    export {};
}
declare namespace ConvertApi {
    interface UploadResponseDto {
        FileId: string;
        FileName: string;
        FileExt: string;
    }
    class FileValue {
        readonly name: string;
        readonly fileId: string;
        constructor(name: string, fileId: string);
    }
    class FileParam implements IParam {
        readonly name: string;
        readonly file: File | FileValue | URL;
        readonly host: string;
        constructor(name: string, file: File | FileValue | URL, host: string);
        value(): Promise<string>;
        get dto(): Promise<IParamDto>;
    }
}
declare namespace ConvertApi {
    class FilesValue {
        private readonly files;
        constructor(files: IResultFileDto[]);
        asArray(): FileValue[];
    }
    class FilesParam implements IParam {
        readonly name: string;
        private fileValPros;
        constructor(name: string, files: string[] | URL[] | FileList | FilesValue, host: string);
        get dto(): Promise<IParamDto>;
    }
}
declare namespace ConvertApi {
    interface IFileValue {
        Id: string;
        Url: string;
    }
    interface IParamDto {
        Name: string;
        Value: string;
        FileValue: IFileValue;
        FileValues: IFileValue[];
    }
    interface IConvertDto {
        Parameters: IParamDto[];
    }
    interface IParam {
        name: string;
        dto: Promise<IParamDto>;
    }
    interface IParams {
        dto: Promise<IConvertDto>;
    }
    class Param implements IParam {
        readonly name: string;
        readonly value: string;
        constructor(name: string, value: string);
        get dto(): Promise<IParamDto>;
    }
}
declare namespace ConvertApi {
    interface IParamInit {
        name: string;
        value: string | string[];
        isFile: boolean;
    }
    class Params {
        private readonly host;
        private readonly params;
        constructor(host: string, init?: IParamInit[]);
        add(name: string, value: string | string[] | File | FileValue | URL | URL[] | FileList | FilesValue): IParam;
        get(name: string): IParam | undefined;
        delete(name: string): IParam | undefined;
        get dto(): Promise<IConvertDto>;
    }
}
declare namespace ConvertApi {
    interface IResultFileDto {
        FileName: string;
        FileExt: string;
        FileSize: number;
        FileId: string;
        Url: string;
    }
    interface IResultDto {
        ConversionTime: number;
        Files: IResultFileDto[];
    }
    class Result {
        private readonly dto;
        constructor(dto: IResultDto);
        get duration(): number;
        get files(): IResultFileDto[];
        toParamFile(idx?: number): FileValue;
        toParamFiles(): FilesValue;
        uploadToS3(region: string, bucket: string, accessKeyId: string, secretAccessKey: string): Promise<Response>[];
    }
}
declare namespace ConvertApi {
    function worker(worker: URL, params: any | HTMLFormElement): Promise<Response>;
}
//# sourceMappingURL=convertapi.d.ts.map