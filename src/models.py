from enum import Enum
from pydantic import BaseModel
from typing import Optional, List, Union


class Orgao(str, Enum):
    tipo_31 = 'FUNDO MUNICIPAL DE SAUDE'
    tipo_32 = 'FUNDO MUNICIPAL DE SAUDE - INFRAESTRUTURA'
    tipo_33 = 'FUNDO MUNICIPAL DE SEGURANCA CIDADA'
    tipo_40 = 'HOSPITAL DISTRITAL  MARIA JOSE BARROSO DE OLIVEIRA'
    tipo_41 = 'HOSPITAL DISTRITAL EDMILSON BARROS DE OLIVEIRA'
    tipo_42 = 'HOSPITAL DISTRITAL EVANDRO AYRES DE MOURA'
    tipo_43 = 'HOSPITAL DISTRITAL GONZAGA MOTA/BARRA DO CEARA'
    tipo_44 = 'HOSPITAL DISTRITAL GONZAGA MOTA/JOSE WALTER'
    tipo_45 = 'HOSPITAL DISTRITAL GONZAGA MOTA/MESSEJANA'
    tipo_46 = 'HOSPITAL E MATERNIDADE DRA ZILDA ARNS NEUMANN'
    tipo_50 = 'INSTITUTO DR. JOSE FROTA'
    tipo_62 = 'SECRETARIA MUNICIPAL DA SAUDE'
    
    
class ResponseSite(BaseModel):
    ID: Optional[Union[int, str]] = ''
    ANOCONTRATO: Optional[Union[int, str]] = ''
    NUMEROCONTRATOSISTEMA: Optional[Union[int, str]] = ''
    NUMEROCONTRATOINSTITUICAO: Optional[Union[int, str]] = ''
    CONTRATADO: Optional[Union[int, str]] = ''
    OBJETOCONTRATO: Optional[Union[int, str]] = ''
    IDUO: Optional[Union[int, str]] = ''
    DESCRICAOUO: Optional[Union[int, str]] = ''
    VALORCONTRATO: Optional[float] = 0.0
    IDCONTRATO: Optional[Union[int, str]] = ''
    ANEXOS: Optional[Union[int, str]] = ''
    QTDADITIVOS: Optional[Union[int, str]] = ''
    CODIGOCOMPLETOUO: Optional[Union[int, str]] = ''
    MODALIDADEPROCESSO: Optional[Union[int, str]] = ''
    MODALIDADEAPLICACAO: Optional[Union[int, str]] = ''
    IDCONTRATOORIGEM: Optional[Union[int, str]] = ''

class ResponseDefault(BaseModel):
    code: int
    message: str
    datetime: str
    results: List[ResponseSite]

class ResponseError(BaseModel):
    code: int
    message: str